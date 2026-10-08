"use client";

import { useState, useEffect, useMemo } from "react";
import {
  Layers,
  Sliders,
  Calendar,
  Eye,
  Info,
  Sparkles,
  MapPin,
  ChevronDown,
  RefreshCw,
  Maximize2,
  CheckSquare,
  Square,
  BarChart3,
  HelpCircle,
} from "lucide-react";
import { fetchRainfallBlend } from "@/lib/api";
import type { RainfallBlendResponse, BlendDistrict } from "@/lib/types";

interface ToggleRainfallMapProps {
  embeddedInBlog?: boolean;
}

const COLOR_SCALE = [
  { min: 1, max: 10, label: "1 - 10 mm", desc: "Light Rain / Drizzle", color: "#33cc66" },
  { min: 10, max: 35, label: "10 - 35 mm", desc: "Moderate Rain", color: "#3399ff" },
  { min: 35, max: 70, label: "35 - 70 mm", desc: "Heavy Rain", color: "#ffcc00" },
  { min: 70, max: 120, label: "70 - 120 mm", desc: "Very Heavy Rain", color: "#ff9900" },
  { min: 120, max: 200, label: "120 - 200 mm", desc: "Extremely Heavy Rain", color: "#cc0000" },
  { min: 200, max: 999, label: "> 200 mm", desc: "Torrential / Exceptional", color: "#ff3399" },
];

export default function ToggleRainfallMap({ embeddedInBlog = false }: ToggleRainfallMapProps) {
  const [day, setDay] = useState<number>(1);
  const [opacity, setOpacity] = useState<number>(0.85);
  const [activeMode, setActiveMode] = useState<"blend" | "ecmwf" | "gfs" | "icon" | "ncum" | "ai">("blend");
  const [showLabels, setShowLabels] = useState<boolean>(true);
  const [selectedDistrict, setSelectedDistrict] = useState<BlendDistrict | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [data, setData] = useState<RainfallBlendResponse | null>(null);

  // Blend Weights (in percentages, sum = 100)
  const [weights, setWeights] = useState({
    ecmwf: 35,
    gfs: 25,
    icon: 20,
    ncum: 10,
    ai: 10,
  });

  // Fetch data on day change
  useEffect(() => {
    async function loadBlend() {
      setLoading(true);
      try {
        const res = await fetchRainfallBlend(day, {
          ecmwf: weights.ecmwf / 100,
          gfs: weights.gfs / 100,
          icon: weights.icon / 100,
          ncum: weights.ncum / 100,
          ai: weights.ai / 100,
        });
        setData(res);
        if (res.districts.length > 0 && !selectedDistrict) {
          setSelectedDistrict(res.districts[0]);
        }
      } catch (err) {
        console.error("Failed to load rainfall blend:", err);
      } finally {
        setLoading(false);
      }
    }
    loadBlend();
  }, [day, weights]);

  // Handle Preset Button clicks
  const applyPreset = (preset: "equal" | "ecmwf_heavy" | "ai_convective") => {
    setActiveMode("blend");
    if (preset === "equal") {
      setWeights({ ecmwf: 20, gfs: 20, icon: 20, ncum: 20, ai: 20 });
    } else if (preset === "ecmwf_heavy") {
      setWeights({ ecmwf: 50, gfs: 25, icon: 15, ncum: 5, ai: 5 });
    } else if (preset === "ai_convective") {
      setWeights({ ecmwf: 25, gfs: 15, icon: 15, ncum: 5, ai: 40 });
    }
  };

  // Map projection coordinates: Tamil Nadu box
  // Lat: 8.0 to 13.6, Lon: 76.0 to 80.5
  const getCoordinates = (lat: number, lon: number) => {
    const minLat = 8.0;
    const maxLat = 13.5;
    const minLon = 76.0;
    const maxLon = 80.6;

    const x = ((lon - minLon) / (maxLon - minLon)) * 520 + 30;
    const y = ((maxLat - lat) / (maxLat - minLat)) * 580 + 30;
    return { x, y };
  };

  const getDistrictRainfall = (district: BlendDistrict) => {
    if (activeMode === "blend") return district.blend_rainfall_mm;
    if (activeMode === "ecmwf") return district.models.ecmwf;
    if (activeMode === "gfs") return district.models.gfs;
    if (activeMode === "icon") return district.models.icon;
    if (activeMode === "ncum") return district.models.ncum;
    if (activeMode === "ai") return district.models.transatunet_ai;
    return district.blend_rainfall_mm;
  };

  const getColorForRain = (mm: number) => {
    if (mm >= 200) return "#ff3399";
    if (mm >= 120) return "#cc0000";
    if (mm >= 70) return "#ff9900";
    if (mm >= 35) return "#ffcc00";
    if (mm >= 10) return "#3399ff";
    if (mm >= 1) return "#33cc66";
    return "#4a5568";
  };

  return (
    <div className={`rounded-2xl border border-teal/30 bg-surface-card overflow-hidden shadow-2xl backdrop-blur-xl ${
      embeddedInBlog ? "my-8" : ""
    }`}>
      {/* ── Top App Bar ── */}
      <div className="bg-gradient-to-r from-deep-blue/80 via-surface to-deep-blue/60 border-b border-border-subtle p-4 sm:p-5 flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-xl bg-teal/20 text-teal border border-teal/40">
            <Sliders className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-lg sm:text-xl font-black text-text-primary tracking-tight">
                24-Hour Rainfall Blend Builder
              </h2>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-accent-rain/20 text-accent-rain border border-accent-rain/40">
                COMK / ChennaiRains Replica
              </span>
            </div>
            <p className="text-xs text-text-secondary mt-0.5">
              Accumulation for 24 hours beginning at 05:30 AM IST · Multi-Model Ensemble Guidance
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          {/* Day Dropdown */}
          <div className="flex items-center gap-2 bg-surface/90 border border-teal/40 px-3 py-1.5 rounded-xl">
            <Calendar className="h-4 w-4 text-teal" />
            <select
              value={day}
              onChange={(e) => setDay(Number(e.target.value))}
              className="bg-transparent text-xs text-text-primary font-bold focus:outline-none cursor-pointer"
            >
              <option value={1} className="bg-surface text-text-primary">Day 1 (05:30 Today - 05:30 Tomorrow)</option>
              <option value={2} className="bg-surface text-text-primary">Day 2 (Next 24-48 Hours)</option>
              <option value={3} className="bg-surface text-text-primary">Day 3 (Next 48-72 Hours)</option>
              <option value={4} className="bg-surface text-text-primary">Day 4 (Next 72-96 Hours)</option>
              <option value={5} className="bg-surface text-text-primary">Day 5 (Next 96-120 Hours)</option>
            </select>
          </div>

          {loading && <RefreshCw className="h-4 w-4 text-teal animate-spin" />}
        </div>
      </div>

      {/* ── Main Workspace: Map Canvas on Left, Blend Controls on Right ── */}
      <div className="grid grid-cols-1 lg:grid-cols-12 min-h-[640px]">
        {/* MAP CANVAS (Col 1-8) */}
        <div className="lg:col-span-8 bg-[#06101E] relative overflow-hidden flex flex-col items-center justify-center p-4 select-none">
          {/* Map Top Status Bar */}
          <div className="absolute top-4 left-4 z-20 flex flex-wrap items-center gap-2">
            <span className="px-3 py-1 rounded-lg bg-surface/90 border border-border-subtle text-xs text-text-primary font-semibold flex items-center gap-1.5 backdrop-blur-md">
              <span className="h-2 w-2 rounded-full" style={{ backgroundColor: getColorForRain(selectedDistrict ? getDistrictRainfall(selectedDistrict) : 0) }} />
              Active Layer:{" "}
              <strong className="text-teal uppercase font-bold">
                {activeMode === "blend" ? "Multi-Model Blend" : activeMode.toUpperCase()}
              </strong>
            </span>
            <span className="px-3 py-1 rounded-lg bg-surface/80 border border-border-subtle text-xs text-text-secondary font-mono">
              {data?.day_label}
            </span>
          </div>

          {/* Quick Opacity & Label Bar */}
          <div className="absolute top-4 right-4 z-20 flex items-center gap-3 bg-surface/90 border border-border-subtle px-3 py-1.5 rounded-xl backdrop-blur-md">
            <span className="text-[11px] text-text-secondary flex items-center gap-1 font-medium">
              <Eye className="h-3.5 w-3.5 text-teal" />
              Opacity: {Math.round(opacity * 100)}%
            </span>
            <input
              type="range"
              min={0.2}
              max={1.0}
              step={0.05}
              value={opacity}
              onChange={(e) => setOpacity(parseFloat(e.target.value))}
              className="w-20 accent-teal cursor-pointer"
            />
            <label className="text-[11px] text-text-secondary flex items-center gap-1 cursor-pointer">
              <input
                type="checkbox"
                checked={showLabels}
                onChange={(e) => setShowLabels(e.target.checked)}
                className="accent-teal rounded"
              />
              Labels
            </label>
          </div>

          {/* SVG Map Canvas: Tamil Nadu & Puducherry Coastline & Districts */}
          <div className="relative w-full max-w-[580px] h-[620px] flex items-center justify-center">
            <svg
              viewBox="0 0 580 640"
              className="w-full h-full"
              style={{ filter: "drop-shadow(0 0 30px rgba(6, 90, 130, 0.25))" }}
            >
              <defs>
                {/* Coastal Glow Gradients */}
                <radialGradient id="oceanGlow" cx="70%" cy="50%" r="60%">
                  <stop offset="0%" stopColor="#065A82" stopOpacity="0.25" />
                  <stop offset="100%" stopColor="#06101E" stopOpacity="0.0" />
                </radialGradient>

                {/* Rain Heatmap Glow Filters */}
                <filter id="rainGlow" x="-50%" y="-50%" width="200%" height="200%">
                  <feGaussianBlur stdDeviation="16" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              {/* Bay of Bengal Ambient Shading */}
              <rect x="0" y="0" width="580" height="640" fill="url(#oceanGlow)" />

              {/* Tamil Nadu Stylized Geographic Coastline Contour */}
              <path
                d="M 120 40 
                   Q 220 50, 340 70 
                   Q 460 90, 520 120 
                   Q 510 180, 480 230 
                   Q 460 270, 470 320 
                   Q 450 380, 430 430 
                   Q 390 490, 340 540 
                   Q 280 600, 220 630 
                   Q 180 580, 150 510 
                   Q 110 420, 90 330 
                   Q 80 230, 90 140 
                   Z"
                fill="#0A182E"
                stroke="#1C7293"
                strokeWidth="2.5"
                strokeDasharray="4 2"
                opacity="0.8"
              />

              {/* Bay of Bengal Water Label */}
              <text x="440" y="240" fill="#1C7293" fontSize="13" fontWeight="bold" opacity="0.4" letterSpacing="4">
                BAY OF BENGAL
              </text>
              <text x="140" y="590" fill="#1C7293" fontSize="11" fontWeight="bold" opacity="0.4" letterSpacing="2">
                INDIAN OCEAN
              </text>
              <text x="60" y="320" fill="#1C7293" fontSize="11" fontWeight="bold" opacity="0.3" transform="rotate(-90 60,320)" letterSpacing="3">
                WESTERN GHATS
              </text>

              {/* Simulated 24-hr Rain Gridded Contours (Heatmap Nodes) */}
              <g style={{ opacity }}>
                {data?.districts.map((d) => {
                  const pt = getCoordinates(d.lat, d.lon);
                  const rain = getDistrictRainfall(d);
                  const color = getColorForRain(rain);
                  const radius = Math.min(65, Math.max(24, rain * 0.95));

                  return (
                    <g key={d.id} className="cursor-pointer group" onClick={() => setSelectedDistrict(d)}>
                      {/* Outer Heatmap Convection Halo */}
                      {rain > 5 && (
                        <circle
                          cx={pt.x}
                          cy={pt.y}
                          r={radius}
                          fill={color}
                          opacity={rain > 70 ? 0.35 : 0.22}
                          filter="url(#rainGlow)"
                        />
                      )}

                      {/* Core Rain Intensity Node */}
                      <circle
                        cx={pt.x}
                        cy={pt.y}
                        r={Math.min(28, Math.max(9, rain * 0.35))}
                        fill={color}
                        stroke="#ffffff"
                        strokeWidth="1.5"
                        opacity={selectedDistrict?.id === d.id ? 1.0 : 0.85}
                        className="transition-transform group-hover:scale-125 duration-200"
                      />

                      {/* District rainfall label on node */}
                      <text
                        x={pt.x}
                        y={pt.y + 4}
                        fill="#0A1628"
                        fontSize="10"
                        fontWeight="black"
                        textAnchor="middle"
                      >
                        {Math.round(rain)}
                      </text>

                      {/* Town / District Label */}
                      {showLabels && (
                        <text
                          x={pt.x}
                          y={pt.y - 14}
                          fill="#E8F1F8"
                          fontSize="9.5"
                          fontWeight={selectedDistrict?.id === d.id ? "bold" : "medium"}
                          textAnchor="middle"
                          className="pointer-events-none"
                          style={{
                            textShadow: "0 1px 3px rgba(0,0,0,0.9), 0 0 5px rgba(0,0,0,0.8)",
                          }}
                        >
                          {d.name.split("/")[0].trim()}
                        </text>
                      )}
                    </g>
                  );
                })}
              </g>
            </svg>
          </div>

          {/* Map Bottom Legend (Replica of ChennaiRains Legend) */}
          <div className="w-full mt-2 pt-3 border-t border-border-subtle/60 flex flex-wrap items-center justify-between gap-3 text-xs z-10 bg-surface/70 px-4 py-2.5 rounded-xl backdrop-blur-md">
            <span className="font-bold text-text-primary text-[11px] uppercase tracking-wider">
              24-Hr Rainfall Scale (mm):
            </span>
            <div className="flex flex-wrap items-center gap-3">
              {COLOR_SCALE.map((item, idx) => (
                <div key={idx} className="flex items-center gap-1.5">
                  <span
                    className="w-3.5 h-3.5 rounded-sm border border-black/40 inline-block shadow-sm"
                    style={{ backgroundColor: item.color }}
                  />
                  <span className="text-[10px] text-text-secondary font-mono font-medium">
                    {item.label}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* ── SIDEBAR: THE RAINFALL BLEND BUILDER (Col 9-12) ── */}
        <div className="lg:col-span-4 bg-surface p-5 sm:p-6 border-t lg:border-t-0 lg:border-l border-border-subtle flex flex-col justify-between space-y-6 overflow-y-auto max-h-[740px]">
          <div className="space-y-6">
            {/* Blend Builder Notice (Exact wording from Chennai Rains) */}
            <div className="p-3.5 rounded-xl bg-teal/10 border border-teal/30 text-xs text-text-secondary leading-relaxed">
              <span className="font-bold text-teal block mb-1 flex items-center gap-1">
                <Info className="h-3.5 w-3.5" />
                Rainfall Blend Builder Guidance
              </span>
              Pick models within categories below. Any subset blends together according to weight ratios. Rainfall accumulation is for 24 hours beginning at 5:30 AM IST.
            </div>

            {/* Mode Category Selector: Blend vs Single Model */}
            <div className="space-y-2">
              <span className="text-xs font-bold text-text-primary uppercase tracking-wider block">
                Guidance Category
              </span>
              <div className="grid grid-cols-2 gap-2">
                <button
                  onClick={() => setActiveMode("blend")}
                  className={`p-2.5 rounded-xl text-xs font-bold transition-all text-center flex items-center justify-center gap-1.5 ${
                    activeMode === "blend"
                      ? "bg-teal text-surface shadow-md shadow-teal/20"
                      : "bg-surface-card border border-border-subtle text-text-secondary hover:text-text-primary"
                  }`}
                >
                  <Sparkles className="h-3.5 w-3.5" />
                  Multi-Model Blend
                </button>
                <button
                  onClick={() => setActiveMode("ecmwf")}
                  className={`p-2.5 rounded-xl text-xs font-bold transition-all text-center flex items-center justify-center gap-1.5 ${
                    activeMode === "ecmwf"
                      ? "bg-teal text-surface shadow-md shadow-teal/20"
                      : "bg-surface-card border border-border-subtle text-text-secondary hover:text-text-primary"
                  }`}
                >
                  <Layers className="h-3.5 w-3.5" />
                  Single Model View
                </button>
              </div>
            </div>

            {/* If Single Model View: Pick Individual Model */}
            {activeMode !== "blend" && (
              <div className="p-4 rounded-xl bg-surface-card border border-border-subtle space-y-2">
                <span className="text-[11px] font-bold text-text-secondary uppercase">
                  Select Deterministic Model
                </span>
                <div className="grid grid-cols-2 gap-1.5">
                  {[
                    { id: "ecmwf", name: "ECMWF IFS (9km)" },
                    { id: "gfs", name: "GFS (13km)" },
                    { id: "icon", name: "ICON DWD (13km)" },
                    { id: "ncum", name: "NCUM India" },
                    { id: "ai", name: "TransAtU-Net AI" },
                  ].map((m) => (
                    <button
                      key={m.id}
                      onClick={() => setActiveMode(m.id as any)}
                      className={`p-2 rounded-lg text-xs font-semibold text-left transition-all ${
                        activeMode === m.id
                          ? "bg-teal/20 border border-teal text-teal"
                          : "bg-white/[0.02] border border-transparent text-text-secondary hover:text-text-primary"
                      }`}
                    >
                      {m.name}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* If Blend Mode: Show Model Weight Sliders & Presets */}
            {activeMode === "blend" && (
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-text-primary uppercase tracking-wider">
                    Model Weights & Consensus
                  </span>
                  <div className="flex gap-1">
                    <button
                      onClick={() => applyPreset("equal")}
                      className="px-2 py-0.5 rounded text-[10px] font-semibold bg-white/5 hover:bg-teal/20 hover:text-teal border border-border-subtle transition-colors"
                    >
                      Equal (20%)
                    </button>
                    <button
                      onClick={() => applyPreset("ecmwf_heavy")}
                      className="px-2 py-0.5 rounded text-[10px] font-semibold bg-white/5 hover:bg-teal/20 hover:text-teal border border-border-subtle transition-colors"
                    >
                      ECMWF (50%)
                    </button>
                    <button
                      onClick={() => applyPreset("ai_convective")}
                      className="px-2 py-0.5 rounded text-[10px] font-semibold bg-white/5 hover:bg-teal/20 hover:text-teal border border-border-subtle transition-colors"
                    >
                      AI Focus (40%)
                    </button>
                  </div>
                </div>

                <div className="space-y-3 bg-surface-card p-4 rounded-xl border border-border-subtle">
                  {/* ECMWF */}
                  <WeightRow
                    label="ECMWF IFS (9km High-Res)"
                    value={weights.ecmwf}
                    onChange={(v) => setWeights({ ...weights, ecmwf: v })}
                    badge="European"
                  />
                  {/* GFS */}
                  <WeightRow
                    label="GFS (NCEP / NOAA 13km)"
                    value={weights.gfs}
                    onChange={(v) => setWeights({ ...weights, gfs: v })}
                    badge="US Global"
                  />
                  {/* ICON */}
                  <WeightRow
                    label="ICON (DWD Germany 13km)"
                    value={weights.icon}
                    onChange={(v) => setWeights({ ...weights, icon: v })}
                    badge="German"
                  />
                  {/* NCUM */}
                  <WeightRow
                    label="NCUM (NCMRWF India 12km)"
                    value={weights.ncum}
                    onChange={(v) => setWeights({ ...weights, ncum: v })}
                    badge="Indian"
                  />
                  {/* TransAtU-Net AI */}
                  <WeightRow
                    label="TransAtU-Net (Our AI Model)"
                    value={weights.ai}
                    onChange={(v) => setWeights({ ...weights, ai: v })}
                    badge="AI Nowcast"
                    highlight
                  />
                </div>
              </div>
            )}

            {/* Selected District Inspector Card */}
            {selectedDistrict && (
              <div className="p-4 rounded-xl bg-surface-card border border-teal/40 space-y-3">
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-teal">
                      {selectedDistrict.region}
                    </span>
                    <h4 className="text-base font-bold text-text-primary">
                      {selectedDistrict.name}
                    </h4>
                  </div>
                  <div className="text-right">
                    <div className="text-xl font-black text-text-primary" style={{ color: getColorForRain(getDistrictRainfall(selectedDistrict)) }}>
                      {getDistrictRainfall(selectedDistrict)} mm
                    </div>
                    <span className="text-[10px] text-text-secondary uppercase">24-Hr Est.</span>
                  </div>
                </div>

                {/* Model Breakdown Bar */}
                <div className="pt-2 border-t border-border-subtle space-y-1.5 text-[11px]">
                  <span className="text-text-secondary font-semibold block text-[10px] uppercase">
                    Model Breakdown for this Station:
                  </span>
                  <div className="grid grid-cols-2 gap-2 text-text-secondary font-mono">
                    <div className="bg-white/[0.02] p-1.5 rounded flex justify-between">
                      <span>ECMWF:</span> <strong className="text-text-primary">{selectedDistrict.models.ecmwf} mm</strong>
                    </div>
                    <div className="bg-white/[0.02] p-1.5 rounded flex justify-between">
                      <span>GFS:</span> <strong className="text-text-primary">{selectedDistrict.models.gfs} mm</strong>
                    </div>
                    <div className="bg-white/[0.02] p-1.5 rounded flex justify-between">
                      <span>ICON:</span> <strong className="text-text-primary">{selectedDistrict.models.icon} mm</strong>
                    </div>
                    <div className="bg-white/[0.02] p-1.5 rounded flex justify-between">
                      <span>NCUM:</span> <strong className="text-text-primary">{selectedDistrict.models.ncum} mm</strong>
                    </div>
                    <div className="bg-teal/10 col-span-2 p-1.5 rounded flex justify-between text-teal">
                      <span>TransAtU-Net AI:</span> <strong>{selectedDistrict.models.transatunet_ai} mm</strong>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Footer citation */}
          <div className="pt-4 border-t border-border-subtle/60 text-[11px] text-text-secondary flex items-center justify-between">
            <span>Data: ECMWF + GFS + Open-Meteo + AI</span>
            <span className="text-teal font-medium">Auto-updated 00Z / 12Z</span>
          </div>
        </div>
      </div>
    </div>
  );
}

function WeightRow({
  label,
  value,
  onChange,
  badge,
  highlight,
}: {
  label: string;
  value: number;
  onChange: (v: number) => void;
  badge: string;
  highlight?: boolean;
}) {
  return (
    <div className={`space-y-1 ${highlight ? "p-2 rounded-lg bg-teal/10 border border-teal/20" : ""}`}>
      <div className="flex items-center justify-between text-xs">
        <span className={`font-semibold ${highlight ? "text-teal" : "text-text-primary"}`}>
          {label}
        </span>
        <span className="font-mono text-xs text-text-secondary font-bold">{value}%</span>
      </div>
      <input
        type="range"
        min={0}
        max={100}
        step={5}
        value={value}
        onChange={(e) => onChange(parseInt(e.target.value))}
        className="w-full accent-teal cursor-pointer h-1.5 bg-surface rounded-lg"
      />
    </div>
  );
}
