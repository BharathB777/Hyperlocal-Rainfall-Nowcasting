"use client";

import { useEffect, useRef } from "react";
import {
  CloudRain,
  Thermometer,
  Droplets,
  Radio,
  ArrowRight,
} from "lucide-react";
import Link from "next/link";
import type { DashboardOverview } from "@/lib/types";

interface HeroWeatherProps {
  overview: DashboardOverview | null;
}

export default function HeroWeather({ overview }: HeroWeatherProps) {
  const rainContainerRef = useRef<HTMLDivElement>(null);

  // Generate CSS rain drops
  useEffect(() => {
    const container = rainContainerRef.current;
    if (!container) return;

    // Create rain drops
    const drops: HTMLDivElement[] = [];
    for (let i = 0; i < 60; i++) {
      const drop = document.createElement("div");
      drop.className = "rain-drop";
      drop.style.left = `${Math.random() * 100}%`;
      drop.style.height = `${Math.random() * 80 + 40}px`;
      drop.style.animationDuration = `${Math.random() * 1.5 + 0.8}s`;
      drop.style.animationDelay = `${Math.random() * 3}s`;
      container.appendChild(drop);
      drops.push(drop);
    }

    return () => {
      drops.forEach((d) => d.remove());
    };
  }, []);

  return (
    <section className="relative min-h-[80vh] flex items-center overflow-hidden gradient-bg">
      {/* Rain animation layer */}
      <div
        ref={rainContainerRef}
        className="absolute inset-0 pointer-events-none overflow-hidden"
      />

      {/* Radial glow */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] rounded-full bg-teal/10 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-0 left-0 right-0 h-40 bg-gradient-to-t from-surface to-transparent pointer-events-none" />

      <div className="relative z-10 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-20 w-full">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left — Text */}
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-accent-rain/10 border border-accent-rain/20 text-accent-rain text-xs font-medium mb-6">
              <Radio className="h-3 w-3 pulse-live" />
              Live Weather Intelligence
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold leading-[1.1] tracking-tight mb-6">
              <span className="text-text-primary">Hyperlocal </span>
              <span className="bg-gradient-to-r from-accent-rain via-teal to-deep-blue bg-clip-text text-transparent">
                Rainfall
              </span>
              <br />
              <span className="text-text-primary">Nowcasting</span>
            </h1>

            <p className="text-lg text-text-secondary leading-relaxed mb-8 max-w-lg">
              Fusing IMD stations, community weather networks, and ECMWF models
              into a single AI-powered platform. Predicting rainfall{" "}
              <span className="text-accent-rain font-semibold">0–3 hours</span>{" "}
              ahead for Tamil Nadu & Puducherry.
            </p>

            <div className="flex flex-wrap gap-4">
              <Link
                href="/dashboard"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-teal to-deep-blue text-white font-semibold text-sm hover:shadow-[0_0_30px_rgba(28,114,147,0.5)] transition-all duration-300 hover:scale-[1.02]"
              >
                Open Dashboard
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link
                href="/forecast"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl border border-border-subtle text-text-secondary font-medium text-sm hover:border-teal hover:text-text-primary transition-all duration-300"
              >
                View Forecast
              </Link>
            </div>
          </div>

          {/* Right — Stats cards */}
          <div className="grid grid-cols-2 gap-4">
            <StatBox
              icon={<Radio className="h-5 w-5 text-accent-green" />}
              label="Active Stations"
              value={overview?.active_stations?.toString() ?? "—"}
              sub="Across TN & Puducherry"
              delay="delay-1"
            />
            <StatBox
              icon={<Thermometer className="h-5 w-5 text-accent-temp" />}
              label="Avg Temperature"
              value={overview?.avg_temp_c != null ? `${overview.avg_temp_c}°C` : "—"}
              sub="Current regional average"
              delay="delay-2"
            />
            <StatBox
              icon={<Droplets className="h-5 w-5 text-accent-rain" />}
              label="Avg Humidity"
              value={overview?.avg_humidity_pct != null ? `${overview.avg_humidity_pct}%` : "—"}
              sub="Relative humidity"
              delay="delay-3"
            />
            <StatBox
              icon={<CloudRain className="h-5 w-5 text-blue-400" />}
              label="Max Rainfall"
              value={overview?.max_rainfall_mm != null ? `${overview.max_rainfall_mm} mm` : "0 mm"}
              sub="In the last 30 min"
              delay="delay-4"
            />
          </div>
        </div>
      </div>
    </section>
  );
}

function StatBox({
  icon,
  label,
  value,
  sub,
  delay,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  sub: string;
  delay: string;
}) {
  return (
    <div className={`glass-card p-5 animate-in ${delay}`}>
      <div className="flex items-center gap-2 mb-3">
        {icon}
        <span className="text-xs font-medium text-text-secondary">{label}</span>
      </div>
      <div className="data-value text-2xl font-bold text-text-primary mb-1">
        {value}
      </div>
      <span className="text-[11px] text-text-secondary">{sub}</span>
    </div>
  );
}
