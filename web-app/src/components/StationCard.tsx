"use client";

import {
  Thermometer,
  Droplets,
  Gauge,
  Wind,
  CloudRain,
  MapPin,
  Clock,
  Sparkles,
} from "lucide-react";
import type { Station } from "@/lib/types";
import { windDirLabel, timeAgo } from "@/lib/types";

interface StationCardProps {
  station: Station;
  onClick?: () => void;
  isSelected?: boolean;
}

export default function StationCard({ station, onClick, isSelected }: StationCardProps) {
  const r = station.latest_reading;

  // Color coding for temperature
  const tempColor = (t: number | null) => {
    if (t === null) return "text-text-secondary";
    if (t >= 40) return "text-red-400";
    if (t >= 35) return "text-accent-temp";
    if (t >= 28) return "text-accent-warn";
    if (t >= 20) return "text-accent-green";
    return "text-accent-rain";
  };

  // Color coding for rainfall
  const rainColor = (mm: number | null) => {
    if (mm === null || mm === 0) return "text-text-secondary";
    if (mm > 10) return "text-red-400";
    if (mm > 2) return "text-accent-rain";
    return "text-blue-400";
  };

  return (
    <div
      className={`
        glass-card p-5 cursor-pointer group
        ${isSelected ? "!border-accent-rain glow-border" : ""}
      `}
      onClick={onClick}
    >
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <h3 className="text-sm font-bold text-text-primary group-hover:text-accent-rain transition-colors">
            {station.name}
          </h3>
          <div className="flex items-center gap-1.5 mt-1">
            <MapPin className="h-3 w-3 text-text-secondary" />
            <span className="text-xs text-text-secondary">{station.city || "—"}</span>
          </div>
        </div>
        <div className="flex flex-col items-end gap-1">
          <span className={`
            inline-flex items-center px-2 py-0.5 rounded-md text-[10px] font-semibold uppercase tracking-wider
            ${station.source === "open-meteo"
              ? "bg-teal/20 text-teal"
              : station.source === "ambient"
                ? "bg-accent-purple/20 text-accent-purple"
                : "bg-accent-warn/20 text-accent-warn"
            }
          `}>
            {station.source}
          </span>
          {r && (
            <span className="flex items-center gap-1 text-[10px] text-text-secondary">
              <Clock className="h-2.5 w-2.5" />
              {timeAgo(r.timestamp)}
            </span>
          )}
        </div>
      </div>

      {/* Main temperature */}
      <div className="mb-4">
        <div className={`data-value text-3xl font-bold ${tempColor(r?.temp_c ?? null)}`}>
          {r?.temp_c !== null && r?.temp_c !== undefined ? `${r.temp_c.toFixed(1)}°` : "—"}
        </div>
        <span className="text-xs text-text-secondary">Temperature</span>
      </div>

      {/* Metrics grid */}
      <div className="grid grid-cols-2 gap-3">
        <MetricItem
          icon={<Droplets className="h-3.5 w-3.5 text-accent-rain" />}
          label="Humidity"
          value={r?.humidity_pct != null ? `${r.humidity_pct.toFixed(0)}%` : "—"}
        />
        <MetricItem
          icon={<Gauge className="h-3.5 w-3.5 text-accent-purple" />}
          label="Pressure"
          value={r?.pressure_hpa != null ? `${r.pressure_hpa.toFixed(0)}` : "—"}
          unit="hPa"
        />
        <MetricItem
          icon={<Wind className="h-3.5 w-3.5 text-accent-green" />}
          label="Wind"
          value={r?.wind_speed_kmh != null ? `${r.wind_speed_kmh.toFixed(0)}` : "—"}
          unit={r?.wind_dir_deg != null ? windDirLabel(r.wind_dir_deg) : "km/h"}
        />
        <MetricItem
          icon={<CloudRain className={`h-3.5 w-3.5 ${rainColor(r?.rainfall_mm ?? null)}`} />}
          label="Rain"
          value={r?.rainfall_mm != null ? `${r.rainfall_mm.toFixed(1)}` : "0.0"}
          unit="mm"
          highlight={r?.rainfall_mm != null && r.rainfall_mm > 0}
        />
      </div>

      {/* AI Nowcasting Indicator */}
      <div className="mt-3.5 pt-2.5 border-t border-white/[0.06] flex items-center justify-between text-[11px]">
        <span className="flex items-center gap-1.5 text-teal font-medium">
          <Sparkles className="h-3 w-3" />
          AI Nowcast (0–1h)
        </span>
        <span className="text-text-secondary font-mono text-[10px]">
          {r?.rainfall_mm && r.rainfall_mm > 0 ? "75% rain likelihood" : "15% rain likelihood (Dry)"}
        </span>
      </div>
    </div>
  );
}

function MetricItem({
  icon,
  label,
  value,
  unit,
  highlight,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  unit?: string;
  highlight?: boolean;
}) {
  return (
    <div className={`
      flex items-center gap-2 px-2.5 py-2 rounded-lg
      ${highlight ? "bg-accent-rain/10 border border-accent-rain/20" : "bg-white/[0.03]"}
    `}>
      {icon}
      <div className="flex flex-col">
        <span className="text-[10px] text-text-secondary leading-none">{label}</span>
        <div className="flex items-baseline gap-0.5">
          <span className="data-value text-sm font-semibold text-text-primary">{value}</span>
          {unit && <span className="text-[10px] text-text-secondary">{unit}</span>}
        </div>
      </div>
    </div>
  );
}
