"use client";

import { useEffect, useState, useRef } from "react";
import StationCard from "@/components/StationCard";
import TrendChart from "@/components/TrendChart";
import Link from "next/link";
import {
  Activity,
  RefreshCw,
  Search,
  Filter,
  MapPin,
  TrendingUp,
  Clock,
  Layers,
  Radio,
  Brain,
} from "lucide-react";
import type { Station, WeatherReading } from "@/lib/types";
import { fetchStationsClient, fetchStationReadingsClient } from "@/lib/api";

export default function DashboardPage() {
  const [stations, setStations] = useState<Station[]>([]);
  const [selectedStation, setSelectedStation] = useState<Station | null>(null);
  const [readings, setReadings] = useState<WeatherReading[]>([]);
  const [loading, setLoading] = useState(true);
  const [chartLoading, setChartLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedSource, setSelectedSource] = useState<string>("all");
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [countdown, setCountdown] = useState<number>(30);

  // Initial load
  useEffect(() => {
    loadStations(true);
  }, []);

  // 30-second auto-poll interval for real-time PWS streaming
  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev <= 1) {
          loadStations(false);
          return 30;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [selectedStation]);

  // Fetch readings when selected station changes
  useEffect(() => {
    if (!selectedStation) return;

    async function loadHistory() {
      setChartLoading(true);
      try {
        const data = await fetchStationReadingsClient(selectedStation!.station_id, 24);
        setReadings(data);
      } catch (err) {
        console.error("Failed to load readings:", err);
      } finally {
        setChartLoading(false);
      }
    }

    loadHistory();
  }, [selectedStation]);

  async function loadStations(isInitial = false) {
    if (isInitial) setLoading(true);
    setIsRefreshing(true);
    try {
      const data = await fetchStationsClient();
      setStations(data);
      if (data.length > 0) {
        setSelectedStation((curr) => {
          if (!curr) return data[0];
          // Keep current selection with refreshed latest_reading
          const updated = data.find((s) => s.station_id === curr.station_id);
          return updated || curr;
        });
      }
    } catch (err) {
      console.error("Failed to load stations:", err);
    } finally {
      setLoading(false);
      setIsRefreshing(false);
    }
  }

  // Filtered stations
  const filteredStations = stations.filter((s) => {
    const matchesSearch =
      s.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (s.city && s.city.toLowerCase().includes(searchQuery.toLowerCase())) ||
      s.station_id.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesSource =
      selectedSource === "all" || s.source === selectedSource;
    return matchesSearch && matchesSource;
  });

  return (
    <div className="min-h-screen py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="h-2.5 w-2.5 rounded-full bg-accent-green pulse-live" />
            <h1 className="text-2xl font-bold text-text-primary tracking-tight">
              Live Observation Dashboard
            </h1>
            <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-teal/20 text-teal border border-teal/30 uppercase tracking-wider">
              PWS + IMD + Open-Meteo
            </span>
          </div>
          <p className="text-sm text-text-secondary">
            Hyperlocal multi-source weather telemetry streaming across Tamil Nadu & Puducherry
          </p>
        </div>

        <div className="flex items-center gap-3">
          {/* Live countdown pill */}
          <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-white/[0.04] border border-border-subtle text-xs text-text-secondary">
            <Radio className="h-3.5 w-3.5 text-accent-rain pulse-live" />
            <span>Auto-sync in <strong className="text-text-primary">{countdown}s</strong></span>
          </div>

          <button
            onClick={() => {
              setCountdown(30);
              loadStations(false);
            }}
            disabled={isRefreshing}
            className="flex items-center gap-2 px-4 py-2 rounded-xl bg-teal/20 border border-teal/40 text-teal hover:bg-teal hover:text-white transition-all text-sm font-semibold shadow-lg shadow-teal/10"
          >
            <RefreshCw className={`h-4 w-4 ${isRefreshing ? "animate-spin" : ""}`} />
            Sync Now
          </button>

          <Link
            href="/forecast"
            className="flex items-center gap-2 px-4 py-2 rounded-xl bg-accent-purple/20 border border-accent-purple/40 text-accent-purple hover:bg-accent-purple hover:text-white transition-all text-sm font-semibold shadow-lg shadow-accent-purple/10"
          >
            <Brain className="h-4 w-4" />
            AI Nowcast Lab
          </Link>
        </div>
      </div>

      {/* Filter & Search Bar */}
      <div className="glass-card p-4 mb-8 flex flex-col sm:flex-row items-center justify-between gap-4">
        {/* Search */}
        <div className="relative w-full sm:w-80">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-text-secondary" />
          <input
            type="text"
            placeholder="Search station, Auroville, Pondy..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-surface border border-border-subtle rounded-xl pl-9 pr-4 py-2 text-sm text-text-primary placeholder:text-text-secondary focus:outline-none focus:border-teal transition-colors"
          />
        </div>

        {/* Source Pills */}
        <div className="flex items-center gap-2 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0">
          <span className="text-xs text-text-secondary flex items-center gap-1 font-medium mr-1">
            <Filter className="h-3 w-3" /> Source:
          </span>
          {["all", "ambient", "open-meteo", "imd"].map((source) => (
            <button
              key={source}
              onClick={() => setSelectedSource(source)}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold uppercase tracking-wider transition-all ${
                selectedSource === source
                  ? "bg-teal text-white shadow-md shadow-teal/30 scale-[1.02]"
                  : "bg-white/5 text-text-secondary hover:text-text-primary hover:bg-white/10"
              }`}
            >
              {source === "all" ? "All Sources" : source === "ambient" ? "Ambient / PWS" : source}
            </button>
          ))}
        </div>
      </div>

      {/* Selected Station Deep Dive & Trend Graph */}
      {selectedStation && (
        <div className="mb-10 animate-in">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <TrendingUp className="h-4 w-4 text-accent-rain" />
              <h2 className="text-lg font-bold text-text-primary">
                Time Series Trend — {selectedStation.name} ({selectedStation.city || "Tamil Nadu"})
              </h2>
              <span className="text-[11px] font-semibold px-2 py-0.5 rounded-md bg-white/10 text-text-secondary uppercase">
                ID: {selectedStation.station_id}
              </span>
            </div>
            <span className="text-xs text-text-secondary flex items-center gap-1">
              <Clock className="h-3 w-3" /> Past 24 Hours
            </span>
          </div>

          {chartLoading ? (
            <div className="glass-card h-80 flex items-center justify-center">
              <div className="flex items-center gap-3 text-text-secondary">
                <RefreshCw className="h-5 w-5 animate-spin text-teal" />
                <span>Loading telemetry trend...</span>
              </div>
            </div>
          ) : (
            <TrendChart readings={readings} height={340} />
          )}
        </div>
      )}

      {/* Stations Grid */}
      <div className="mb-6 flex items-center justify-between">
        <h2 className="text-lg font-bold text-text-primary flex items-center gap-2">
          <Layers className="h-4 w-4 text-teal" />
          Active Stations ({filteredStations.length})
        </h2>
        <span className="text-xs text-text-secondary">
          Click any station card to inspect telemetry graphs
        </span>
      </div>

      {loading ? (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="glass-card p-5 h-64 animate-pulse">
              <div className="h-4 w-28 bg-white/10 rounded mb-4" />
              <div className="h-10 w-20 bg-white/10 rounded mb-6" />
              <div className="grid grid-cols-2 gap-3">
                <div className="h-12 bg-white/5 rounded" />
                <div className="h-12 bg-white/5 rounded" />
                <div className="h-12 bg-white/5 rounded" />
                <div className="h-12 bg-white/5 rounded" />
              </div>
            </div>
          ))}
        </div>
      ) : filteredStations.length === 0 ? (
        <div className="glass-card p-12 text-center">
          <MapPin className="h-8 w-8 text-text-secondary mx-auto mb-3 opacity-50" />
          <p className="text-text-primary font-semibold mb-1">No stations found</p>
          <p className="text-xs text-text-secondary">Try adjusting your search query or source filter</p>
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {filteredStations.map((station) => (
            <StationCard
              key={station.station_id}
              station={station}
              isSelected={selectedStation?.station_id === station.station_id}
              onClick={() => setSelectedStation(station)}
            />
          ))}
        </div>
      )}
    </div>
  );
}
