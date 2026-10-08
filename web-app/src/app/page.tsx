"use client";

import { useEffect, useState } from "react";
import HeroWeather from "@/components/HeroWeather";
import StationCard from "@/components/StationCard";
import {
  Layers,
  Brain,
  Satellite,
  Database,
  ArrowRight,
} from "lucide-react";
import Link from "next/link";
import type { DashboardOverview, Station } from "@/lib/types";
import { fetchOverviewClient, fetchStationsClient } from "@/lib/api";

export default function HomePage() {
  const [overview, setOverview] = useState<DashboardOverview | null>(null);
  const [stations, setStations] = useState<Station[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const [ov, st] = await Promise.all([
          fetchOverviewClient(),
          fetchStationsClient(),
        ]);
        setOverview(ov);
        setStations(st);
      } catch (err) {
        console.error("Failed to load data:", err);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <HeroWeather overview={overview} />

      {/* Architecture Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="text-center mb-14">
            <h2 className="text-3xl font-bold text-text-primary mb-3">
              Three-Layer Intelligence
            </h2>
            <p className="text-text-secondary max-w-2xl mx-auto">
              Each layer targets a distinct time horizon, fused into a single coherent platform.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            <LayerCard
              icon={<Satellite className="h-6 w-6" />}
              title="Observation Layer"
              subtitle="What's happening right now"
              description="IMD AWS stations and community Personal Weather Stations (PWS) provide ground-truth observations at hyperlocal resolution."
              color="accent-green"
              delay="delay-1"
            />
            <LayerCard
              icon={<Database className="h-6 w-6" />}
              title="NWP Layer"
              subtitle="What's expected (1-10 days)"
              description="ECMWF Open Data numerical weather prediction models give multi-day regional forecasts for temperature, rainfall, and pressure."
              color="accent-purple"
              delay="delay-2"
            />
            <Link href="/forecast" className="group">
              <LayerCard
                icon={<Brain className="h-6 w-6 group-hover:scale-110 transition-transform text-accent-rain" />}
                title="AI Nowcast Layer"
                subtitle="What's about to happen (0-2 hrs)"
                description="Custom deep learning engine implementing LSTMAtU-Net (DSC U-Net + ECSA Attention + Vertical ConvLSTM) and Spatio-Temporal Transformers to forecast hyperlocal precipitation."
                color="accent-rain"
                delay="delay-3"
              />
            </Link>
          </div>
        </div>
      </section>

      {/* Live Stations Preview */}
      <section className="py-16 px-4 sm:px-6 lg:px-8 border-t border-border-subtle">
        <div className="mx-auto max-w-7xl">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h2 className="text-2xl font-bold text-text-primary mb-1">
                Live Stations
              </h2>
              <p className="text-sm text-text-secondary">
                {loading ? "Loading..." : `${stations.length} stations reporting across Tamil Nadu & Puducherry`}
              </p>
            </div>
            <Link
              href="/dashboard"
              className="flex items-center gap-1.5 text-sm text-teal hover:text-accent-rain transition-colors font-medium"
            >
              Full Dashboard
              <ArrowRight className="h-4 w-4" />
            </Link>
          </div>

          {loading ? (
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="glass-card p-5 h-56 animate-pulse">
                  <div className="h-3 w-24 bg-white/10 rounded mb-4" />
                  <div className="h-8 w-16 bg-white/10 rounded mb-6" />
                  <div className="grid grid-cols-2 gap-3">
                    <div className="h-12 bg-white/5 rounded" />
                    <div className="h-12 bg-white/5 rounded" />
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {stations.slice(0, 4).map((station) => (
                <StationCard key={station.station_id} station={station} />
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Tech Stack Banner */}
      <section className="py-12 px-4 sm:px-6 lg:px-8 bg-midnight/30 border-t border-border-subtle">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-wrap items-center justify-center gap-8 text-text-secondary text-sm">
            {["Next.js", "FastAPI", "PyTorch", "ECMWF", "Open-Meteo", "TimescaleDB", "Recharts"].map((tech) => (
              <span key={tech} className="flex items-center gap-1.5 hover:text-text-primary transition-colors">
                <Layers className="h-3.5 w-3.5" />
                {tech}
              </span>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}

function LayerCard({
  icon,
  title,
  subtitle,
  description,
  color,
  delay,
}: {
  icon: React.ReactNode;
  title: string;
  subtitle: string;
  description: string;
  color: string;
  delay: string;
}) {
  return (
    <div className={`glass-card p-7 animate-in ${delay}`}>
      <div className={`inline-flex items-center justify-center h-12 w-12 rounded-xl bg-${color}/15 text-${color} mb-5`}>
        {icon}
      </div>
      <h3 className="text-lg font-bold text-text-primary mb-1">{title}</h3>
      <p className={`text-xs font-semibold text-${color} uppercase tracking-wider mb-3`}>
        {subtitle}
      </p>
      <p className="text-sm text-text-secondary leading-relaxed">{description}</p>
    </div>
  );
}
