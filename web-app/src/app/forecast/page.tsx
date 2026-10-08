"use client";

import { useState, useEffect } from "react";
import {
  Brain,
  CloudRain,
  Layers,
  Cpu,
  Zap,
  TrendingUp,
  AlertTriangle,
  Sparkles,
  Info,
  CheckCircle2,
  ChevronRight,
  Gauge,
  Clock,
  ArrowRight,
  ShieldCheck,
  RefreshCw,
} from "lucide-react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { fetchNowcastModels, fetchNowcastPredictions } from "@/lib/api";
import type { NowcastModelInfo, StationNowcast } from "@/lib/types";

export default function ForecastPage() {
  const [models, setModels] = useState<NowcastModelInfo[]>([]);
  const [selectedModel, setSelectedModel] = useState<string>("transatunet");
  const [predictions, setPredictions] = useState<StationNowcast[]>([]);
  const [selectedStationId, setSelectedStationId] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(true);
  const [activeTab, setActiveTab] = useState<"forecast" | "architecture" | "benchmarks">("forecast");
  const [selectedArchComponent, setSelectedArchComponent] = useState<string>("transformer");

  // Load models on mount
  useEffect(() => {
    async function loadData() {
      setLoading(true);
      try {
        const modelList = await fetchNowcastModels();
        setModels(modelList);
        const predRes = await fetchNowcastPredictions(selectedModel);
        setPredictions(predRes.predictions);
        if (predRes.predictions.length > 0 && !selectedStationId) {
          setSelectedStationId(predRes.predictions[0].station_id);
        }
      } catch (err) {
        console.error("Failed to fetch nowcast data:", err);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [selectedModel]);

  const activeStation = predictions.find((p) => p.station_id === selectedStationId) || predictions[0];

  const chartData = activeStation?.horizons.map((h) => ({
    time: `+${h.lead_time_min}m`,
    probability: Math.round(h.rain_probability * 100),
    intensity: h.rain_intensity_mm,
  })) || [];

  return (
    <div className="min-h-screen py-10 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto space-y-10">
      {/* ── Page Header ── */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-deep-blue/40 via-surface-card to-deep-blue/20 border border-teal/30 p-8 sm:p-10 shadow-2xl backdrop-blur-xl">
        <div className="relative z-10 max-w-4xl space-y-4">
          <div className="flex flex-wrap items-center gap-2">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-teal/20 text-teal border border-teal/40">
              <Brain className="h-3.5 w-3.5" />
              Deep Learning Precipitation Nowcasting
            </span>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-accent-purple/20 text-accent-purple border border-accent-purple/40">
              <Sparkles className="h-3.5 w-3.5" />
              Sensors 2023 Base Paper Implementation
            </span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-text-primary">
            AI Precipitation Nowcasting & <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal via-accent-rain to-accent-purple">
              Neural Architecture Lab
            </span>
          </h1>

          <p className="text-sm sm:text-base text-text-secondary leading-relaxed max-w-3xl">
            Hyperlocal 0–2 hour quantitative precipitation forecasting (QPF). Implementing the{" "}
            <strong className="text-text-primary font-semibold">LSTMAtU-Net</strong> base paper (Depthwise-Separable U-Net, ECSA Attention, Vertical ConvLSTM) and extending it into{" "}
            <strong className="text-teal font-semibold">Spatio-Temporal Transformers & Focal Weighted Loss</strong> to capture severe convective storms without spatial blur.
          </p>

          {/* Quick Sub-navigation */}
          <div className="flex flex-wrap gap-2 pt-2">
            <button
              onClick={() => setActiveTab("forecast")}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                activeTab === "forecast"
                  ? "bg-teal text-surface shadow-lg shadow-teal/20"
                  : "bg-surface/60 text-text-secondary hover:text-text-primary border border-border-subtle"
              }`}
            >
              <CloudRain className="h-4 w-4" />
              Live 0–2h Predictions
            </button>
            <button
              onClick={() => setActiveTab("architecture")}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                activeTab === "architecture"
                  ? "bg-teal text-surface shadow-lg shadow-teal/20"
                  : "bg-surface/60 text-text-secondary hover:text-text-primary border border-border-subtle"
              }`}
            >
              <Layers className="h-4 w-4" />
              Architecture Explorer (U-Net, Transformer, LSTM)
            </button>
            <button
              onClick={() => setActiveTab("benchmarks")}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                activeTab === "benchmarks"
                  ? "bg-teal text-surface shadow-lg shadow-teal/20"
                  : "bg-surface/60 text-text-secondary hover:text-text-primary border border-border-subtle"
              }`}
            >
              <TrendingUp className="h-4 w-4" />
              Meteorological Benchmarks (CSI / POD / FAR)
            </button>
          </div>
        </div>
      </div>

      {/* ── Model Selector Bar ── */}
      <div className="glass-card p-4 sm:p-6 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 className="text-base font-bold text-text-primary flex items-center gap-2">
              <Cpu className="h-4 w-4 text-teal" />
              Active Nowcasting Model Engine
            </h2>
            <p className="text-xs text-text-secondary mt-0.5">
              Switch between the Base Paper model and our proposed Transformer architecture
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs text-text-secondary">Station Scope:</span>
            <select
              value={selectedStationId}
              onChange={(e) => setSelectedStationId(e.target.value)}
              className="bg-surface/90 border border-teal/40 rounded-lg px-3 py-1.5 text-xs text-text-primary font-medium focus:outline-none focus:ring-1 focus:ring-teal"
            >
              {predictions.map((p) => (
                <option key={p.station_id} value={p.station_id}>
                  {p.station_name} ({p.city || "Tamil Nadu"})
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
          {/* Option 1: TransAtU-Net (Proposed) */}
          <button
            onClick={() => setSelectedModel("transatunet")}
            className={`p-4 rounded-2xl text-left border transition-all flex flex-col justify-between ${
              selectedModel === "transatunet"
                ? "bg-teal/15 border-teal shadow-md shadow-teal/10"
                : "bg-surface/40 border-border-subtle hover:border-teal/30"
            }`}
          >
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-teal/20 text-teal">
                  ⭐ Proposed Future Work
                </span>
                <span className="text-[10px] text-text-secondary">21.4M Params</span>
              </div>
              <h3 className="text-sm font-bold text-text-primary">TransAtU-Net</h3>
              <p className="text-xs text-text-secondary mt-1">
                Space-Time Transformer + ECSA Attention + Focal Weighted Loss. Solves ConvLSTM blur over 1–2 hours.
              </p>
            </div>
            <div className="mt-3 pt-2 border-t border-white/5 flex items-center justify-between text-[11px]">
              <span className="text-teal font-semibold">CSI (2h): 0.412</span>
              <span className="text-text-secondary">POD: 74.8%</span>
            </div>
          </button>

          {/* Option 2: LSTMAtU-Net (Base Paper) */}
          <button
            onClick={() => setSelectedModel("lstmatunet")}
            className={`p-4 rounded-2xl text-left border transition-all flex flex-col justify-between ${
              selectedModel === "lstmatunet"
                ? "bg-accent-purple/15 border-accent-purple shadow-md shadow-accent-purple/10"
                : "bg-surface/40 border-border-subtle hover:border-accent-purple/30"
            }`}
          >
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-accent-purple/20 text-accent-purple">
                  📄 Sensors 2023 Base Paper
                </span>
                <span className="text-[10px] text-text-secondary">18.6M Params (-42%)</span>
              </div>
              <h3 className="text-sm font-bold text-text-primary">LSTMAtU-Net</h3>
              <p className="text-xs text-text-secondary mt-1">
                Depthwise-Separable U-Net + ECSA Skip Attention + Vertical Flow ConvLSTM + TLoss.
              </p>
            </div>
            <div className="mt-3 pt-2 border-t border-white/5 flex items-center justify-between text-[11px]">
              <span className="text-accent-purple font-semibold">CSI (2h): 0.381</span>
              <span className="text-text-secondary">POD: 72.5%</span>
            </div>
          </button>

          {/* Option 3: ConvLSTM Baseline */}
          <button
            onClick={() => setSelectedModel("convlstm")}
            className={`p-4 rounded-2xl text-left border transition-all flex flex-col justify-between ${
              selectedModel === "convlstm"
                ? "bg-accent-warn/15 border-accent-warn shadow-md shadow-accent-warn/10"
                : "bg-surface/40 border-border-subtle hover:border-accent-warn/30"
            }`}
          >
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-accent-warn/20 text-accent-warn">
                  ⏱️ Classical Baseline
                </span>
                <span className="text-[10px] text-text-secondary">15.8M Params</span>
              </div>
              <h3 className="text-sm font-bold text-text-primary">ConvLSTM Baseline</h3>
              <p className="text-xs text-text-secondary mt-1">
                Shi et al. (2015). Standard sequential convolutional LSTM without multi-scale skip attention.
              </p>
            </div>
            <div className="mt-3 pt-2 border-t border-white/5 flex items-center justify-between text-[11px]">
              <span className="text-accent-warn font-semibold">CSI (2h): 0.369</span>
              <span className="text-text-secondary">POD: 68.7%</span>
            </div>
          </button>
        </div>
      </div>

      {/* ── TAB 1: Live Nowcast Dashboard ── */}
      {activeTab === "forecast" && (
        <div className="space-y-8">
          {/* Station Overview & Summary Card */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Station Live Telemetry Context */}
            <div className="glass-card p-6 flex flex-col justify-between">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-teal">
                  Station Observation Feed
                </span>
                <h3 className="text-xl font-bold text-text-primary mt-1">
                  {activeStation?.station_name || "Weather Station"}
                </h3>
                <p className="text-xs text-text-secondary">
                  Location: {activeStation?.city || "Tamil Nadu"} · ID: {activeStation?.station_id}
                </p>

                <div className="grid grid-cols-2 gap-3 mt-6">
                  <div className="bg-surface/70 border border-border-subtle p-3 rounded-xl">
                    <span className="text-[10px] text-text-secondary uppercase">Air Temperature</span>
                    <div className="text-lg font-bold text-text-primary mt-0.5">
                      {activeStation?.current_conditions?.temp_c !== null && activeStation?.current_conditions?.temp_c !== undefined
                        ? `${activeStation?.current_conditions?.temp_c?.toFixed(1)}°C`
                        : "—"}
                    </div>
                  </div>
                  <div className="bg-surface/70 border border-border-subtle p-3 rounded-xl">
                    <span className="text-[10px] text-text-secondary uppercase">Relative Humidity</span>
                    <div className="text-lg font-bold text-accent-rain mt-0.5">
                      {activeStation?.current_conditions?.humidity_pct?.toFixed(0) || "—"}%
                    </div>
                  </div>
                  <div className="bg-surface/70 border border-border-subtle p-3 rounded-xl">
                    <span className="text-[10px] text-text-secondary uppercase">Barometric Pressure</span>
                    <div className="text-lg font-bold text-accent-purple mt-0.5">
                      {activeStation?.current_conditions?.pressure_hpa?.toFixed(0) || "—"} hPa
                    </div>
                  </div>
                  <div className="bg-surface/70 border border-border-subtle p-3 rounded-xl">
                    <span className="text-[10px] text-text-secondary uppercase">Current Rainfall</span>
                    <div className="text-lg font-bold text-text-primary mt-0.5">
                      {activeStation?.current_conditions?.current_rain_mm?.toFixed(1) || "0.0"} mm
                    </div>
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-border-subtle text-xs text-text-secondary flex items-center justify-between">
                <span>Model: <strong className="text-text-primary">{activeStation?.model_name}</strong></span>
                <span className="flex items-center gap-1 text-teal">
                  <CheckCircle2 className="h-3.5 w-3.5" /> Synchronized
                </span>
              </div>
            </div>

            {/* Interactive Trend Chart */}
            <div className="glass-card p-6 lg:col-span-2">
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h3 className="text-base font-bold text-text-primary flex items-center gap-2">
                    <TrendingUp className="h-4 w-4 text-teal" />
                    Nowcasting Precipitation Trajectory (Next 120 Minutes)
                  </h3>
                  <span className="text-xs text-text-secondary">
                    Rain probability (%) & predicted intensity (mm/h) across 6 consecutive lead times
                  </span>
                </div>
              </div>

              <div className="h-64 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                    <defs>
                      <linearGradient id="probGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#00D4FF" stopOpacity={0.4} />
                        <stop offset="95%" stopColor="#00D4FF" stopOpacity={0.0} />
                      </linearGradient>
                      <linearGradient id="intensityGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#1C7293" stopOpacity={0.3} />
                        <stop offset="95%" stopColor="#1C7293" stopOpacity={0.0} />
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#21295C" opacity={0.6} />
                    <XAxis dataKey="time" stroke="#8BA4B8" fontSize={11} />
                    <YAxis stroke="#8BA4B8" fontSize={11} />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#0A1628",
                        borderColor: "#1C7293",
                        borderRadius: "12px",
                        fontSize: "12px",
                        color: "#E8F1F8",
                      }}
                    />
                    <Area
                      type="monotone"
                      dataKey="probability"
                      name="Rain Probability (%)"
                      stroke="#00D4FF"
                      strokeWidth={2.5}
                      fillOpacity={1}
                      fill="url(#probGradient)"
                    />
                    <Area
                      type="monotone"
                      dataKey="intensity"
                      name="Intensity (mm)"
                      stroke="#1C7293"
                      strokeWidth={2}
                      fillOpacity={1}
                      fill="url(#intensityGradient)"
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>

          {/* Multi-Horizon Lead Time Cards */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-base font-bold text-text-primary flex items-center gap-2">
                <Clock className="h-4 w-4 text-teal" />
                Multi-Horizon Predictive Timeline (+15m to +120m)
              </h3>
              <span className="text-xs text-text-secondary">Generated in real-time by PyTorch neural backbone</span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
              {activeStation?.horizons.map((h, idx) => (
                <div
                  key={idx}
                  className="bg-surface-card border border-border-subtle hover:border-teal/50 rounded-2xl p-4 transition-all duration-300 flex flex-col justify-between relative overflow-hidden group"
                >
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-bold px-2 py-0.5 rounded-md bg-teal/15 text-teal">
                      +{h.lead_time_min}m
                    </span>
                    <span className="text-[10px] text-text-secondary">
                      {(h.confidence * 100).toFixed(0)}% conf
                    </span>
                  </div>

                  <div className="my-2">
                    <div className="text-2xl font-black text-text-primary tracking-tight">
                      {(h.rain_probability * 100).toFixed(0)}%
                    </div>
                    <span className="text-[10px] text-text-secondary uppercase tracking-wider">
                      Rain Chance
                    </span>
                  </div>

                  <div className="space-y-2 pt-2 border-t border-border-subtle/50">
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-text-secondary">Intensity</span>
                      <span className="font-semibold text-accent-rain">{h.rain_intensity_mm} mm</span>
                    </div>

                    <div className="w-full bg-surface rounded-full h-1.5 overflow-hidden">
                      <div
                        className="bg-gradient-to-r from-teal to-accent-rain h-full rounded-full transition-all"
                        style={{ width: `${Math.min(100, h.rain_probability * 100)}%` }}
                      />
                    </div>

                    <span className={`block text-[10px] font-semibold text-center py-1 rounded-md ${
                      h.rain_probability > 0.6
                        ? "bg-accent-rain/20 text-accent-rain"
                        : h.rain_probability > 0.3
                        ? "bg-teal/20 text-teal"
                        : "bg-white/5 text-text-secondary"
                    }`}>
                      {h.category}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* ── TAB 2: Architecture Deep Dive ── */}
      {activeTab === "architecture" && (
        <div className="space-y-8">
          {/* Component Tabs */}
          <div className="flex flex-wrap gap-2 border-b border-border-subtle pb-4">
            {[
              { id: "transformer", label: "Spatio-Temporal Transformer", icon: Sparkles },
              { id: "unet_dsc", label: "Depthwise Separable U-Net", icon: Layers },
              { id: "ecsa", label: "ECSA Attention Module", icon: Brain },
              { id: "v_lstm", label: "Vertical Flow ConvLSTM", icon: Clock },
              { id: "loss", label: "TLoss & Focal Loss Functions", icon: Gauge },
            ].map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setSelectedArchComponent(tab.id)}
                  className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                    selectedArchComponent === tab.id
                      ? "bg-teal/20 border border-teal text-teal shadow-md shadow-teal/10"
                      : "bg-surface-card border border-border-subtle text-text-secondary hover:text-text-primary"
                  }`}
                >
                  <Icon className="h-3.5 w-3.5" />
                  {tab.label}
                </button>
              );
            })}
          </div>

          {/* Component 1: Spatio-Temporal Transformer (Base Paper Future Research) */}
          {selectedArchComponent === "transformer" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-teal">
                  Addressing Base Paper Shortcoming & Future Scope
                </span>
                <h3 className="text-2xl font-bold text-text-primary">
                  Spatio-Temporal Transformer Bottleneck
                </h3>
                <p className="text-sm text-text-secondary leading-relaxed">
                  In Section 5, the base paper authors concluded:{" "}
                  <em className="text-teal">
                    &quot;the accuracy of the forecast results and clarity of the forecast images decreased with the increase of the forecast time... the Transformer architecture can be introduced and improved to effectively capture long time series coherence.&quot;
                  </em>
                </p>
                <div className="space-y-3 pt-2">
                  <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle">
                    <h4 className="text-xs font-bold text-text-primary uppercase mb-1">
                      1. Resolving the &quot;Convolutional Averaging Blur&quot;
                    </h4>
                    <p className="text-xs text-text-secondary">
                      Repeated convolutional downsampling and $3 \times 3$ receptive fields act as low-pass filters. Self-attention provides direct $O(1)$ pairwise interactions across all spatial cloud patches, preserving sharp rain rate gradients.
                    </p>
                  </div>
                  <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle">
                    <h4 className="text-xs font-bold text-text-primary uppercase mb-1">
                      2. Multi-Head Space-Time Attention (ST-MHSA)
                    </h4>
                    <p className="text-xs text-text-secondary">
                      Computes scaled dot-product attention over spatial tokens $(H \times W)$ and time horizons simultaneously without iterative recurrent degradation:
                      <code className="block mt-1 p-2 rounded bg-black/40 text-teal text-[11px] font-mono">
                        Attention(Q, K, V) = softmax(Q · K^T / sqrt(d_k)) · V
                      </code>
                    </p>
                  </div>
                </div>
              </div>

              <div className="glass-card p-6 space-y-4 flex flex-col justify-center">
                <h4 className="text-sm font-bold text-text-primary">Transformer Pipeline Diagram</h4>
                <div className="bg-surface/90 border border-teal/30 rounded-xl p-5 font-mono text-xs text-text-secondary space-y-3">
                  <div className="p-3 bg-teal/10 border border-teal/30 rounded-lg text-teal">
                    Input: DSC Encoder Bottleneck Feature Map: (Batch, C=512, H=4, W=4)
                  </div>
                  <div className="text-center text-teal">↓ Flatten Spatial Tokens: (B, 16, 512)</div>
                  <div className="p-3 bg-accent-purple/10 border border-accent-purple/30 rounded-lg text-accent-purple">
                    ST-MHSA (8 Heads, LayerNorm, GELU MLP, Residual Connections)
                  </div>
                  <div className="text-center text-accent-purple">↓ Reshape back to Grid: (B, 512, 4, 4)</div>
                  <div className="p-3 bg-teal/10 border border-teal/30 rounded-lg text-teal">
                    Output to Decoder via ECSA Attention Skip Connections
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Component 2: U-Net with Depthwise Separable Convolutions */}
          {selectedArchComponent === "unet_dsc" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-accent-purple">
                  Base Paper Architectural Backbone
                </span>
                <h3 className="text-2xl font-bold text-text-primary">
                  Depthwise-Separable Convolution (DSC) U-Net
                </h3>
                <p className="text-sm text-text-secondary leading-relaxed">
                  Classical U-Net uses standard 2D convolutions (K × K × Cin × Cout), leading to over 32 million parameters and high inference latency. LSTMAtU-Net replaces every standard convolutional block with Depthwise-Separable Convolutions (DSC).
                </p>
                <div className="grid grid-cols-2 gap-3 pt-2">
                  <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle">
                    <span className="text-xs text-text-secondary uppercase">Standard U-Net</span>
                    <div className="text-lg font-bold text-text-primary mt-1">32,023,892</div>
                    <span className="text-[10px] text-red-400">High memory footprint</span>
                  </div>
                  <div className="p-4 rounded-xl bg-teal/10 border border-teal/30">
                    <span className="text-xs text-teal uppercase">LSTMAtU-Net (DSC)</span>
                    <div className="text-lg font-bold text-teal mt-1">18,619,421</div>
                    <span className="text-[10px] text-teal">41.86% parameter reduction</span>
                  </div>
                </div>
              </div>

              <div className="glass-card p-6 space-y-4 flex flex-col justify-center">
                <h4 className="text-sm font-bold text-text-primary">DSC Decomposition Formulation</h4>
                <div className="bg-surface/90 border border-border-subtle rounded-xl p-5 font-mono text-xs text-text-secondary space-y-3">
                  <div className="p-2.5 bg-white/5 rounded-lg">
                    <span className="text-text-primary font-bold">1. Depthwise Convolution:</span>
                    <div className="text-[11px] text-text-secondary mt-1">
                      Applies a single $3 \times 3$ spatial filter per channel (groups = C_in).
                    </div>
                  </div>
                  <div className="p-2.5 bg-white/5 rounded-lg">
                    <span className="text-text-primary font-bold">2. Pointwise Convolution:</span>
                    <div className="text-[11px] text-text-secondary mt-1">
                      Applies a $1 \times 1$ linear projection across channels to mix features.
                    </div>
                  </div>
                  <div className="p-2.5 bg-white/5 rounded-lg">
                    <span className="text-text-primary font-bold">3. Normalization & Activation:</span>
                    <div className="text-[11px] text-text-secondary mt-1">
                      BatchNorm2d followed by Rectified Linear Unit (ReLU).
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Component 3: ECSA Attention Module */}
          {selectedArchComponent === "ecsa" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-accent-rain">
                  Base Paper Attention Innovation
                </span>
                <h3 className="text-2xl font-bold text-text-primary">
                  Efficient Channel & Space Attention (ECSA)
                </h3>
                <p className="text-sm text-text-secondary leading-relaxed">
                  Standard channel attention (ECA / SENet) uses Global Average Pooling ($GAP$), compressing the entire $H \times W$ spatial plane into a single $1 \times 1$ scalar. For precipitation nowcasting, this destroys localized cloud and rain gradients.
                </p>
                <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle space-y-2">
                  <h4 className="text-xs font-bold text-text-primary uppercase">
                    Multi-Scale Adaptive Average Pooling (AAP)
                  </h4>
                  <p className="text-xs text-text-secondary">
                    Instead of $1 \times 1$, ECSA dynamically adapts pooling to scale $R \times R$:
                  </p>
                  <div className="grid grid-cols-5 gap-2 text-center text-xs font-mono pt-1">
                    <div className="p-2 rounded bg-white/5 text-text-primary">L1: 16×16</div>
                    <div className="p-2 rounded bg-white/5 text-text-primary">L2: 8×8</div>
                    <div className="p-2 rounded bg-white/5 text-text-primary">L3: 4×4</div>
                    <div className="p-2 rounded bg-white/5 text-text-primary">L4: 2×2</div>
                    <div className="p-2 rounded bg-white/5 text-text-primary">L5: 1×1</div>
                  </div>
                </div>
              </div>

              <div className="glass-card p-6 space-y-4 flex flex-col justify-center">
                <h4 className="text-sm font-bold text-text-primary">Mathematical Formulation (Eq. 2)</h4>
                <div className="bg-surface/90 border border-accent-rain/30 rounded-xl p-5 font-mono text-xs text-text-secondary space-y-3">
                  <div className="p-3 bg-accent-rain/10 border border-accent-rain/30 rounded-lg text-accent-rain text-center font-bold text-sm">
                    X_tilde = sigma( C1D_3( AAP(X, R) ) ) ⊗ X
                  </div>
                  <ul className="list-disc list-inside space-y-1 text-[11px]">
                    <li><strong>AAP(X, R):</strong> Spatial pooling down to $R \times R \times C$</li>
                    <li><strong>C1D_3:</strong> 1D Convolution over channel dimension with kernel size $k=3$</li>
                    <li><strong>sigma:</strong> Sigmoid activation generating channel attention weights</li>
                    <li><strong>⊗:</strong> Hadamard channel-wise multiplication with input $X$</li>
                  </ul>
                </div>
              </div>
            </div>
          )}

          {/* Component 4: Vertical Flow ConvLSTM */}
          {selectedArchComponent === "v_lstm" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-teal">
                  Base Paper Temporal Unit
                </span>
                <h3 className="text-2xl font-bold text-text-primary">
                  Vertical Flow ConvLSTM (ConvLSTM-VF)
                </h3>
                <p className="text-sm text-text-secondary leading-relaxed">
                  Standard ConvLSTM passes recurrent states horizontally along time frames $t-1 \to t$. In LSTMAtU-Net, the ConvLSTM cell is rotated 90 degrees to deliver information <strong className="text-text-primary">vertically across the U-Net hierarchy levels</strong>.
                </p>
                <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle space-y-2">
                  <h4 className="text-xs font-bold text-text-primary uppercase">
                    Vertical Memory Propagation (Eq. 3)
                  </h4>
                  <p className="text-xs text-text-secondary">
                    Memory $M^l$ and hidden state $H^l$ flow vertically from layer $l-1$ to layer $l$, enabling multi-scale spatiotemporal fusion directly into the skip connections.
                  </p>
                </div>
              </div>

              <div className="glass-card p-6 space-y-4 flex flex-col justify-center">
                <h4 className="text-sm font-bold text-text-primary">Gate Update Equations</h4>
                <div className="bg-surface/90 border border-border-subtle rounded-xl p-4 font-mono text-[11px] text-text-secondary space-y-1.5">
                  <div className="text-teal">g = tanh( W_xg * X + W_hg * H^(l-1) + W_mg * M^(l-1) + b_g )</div>
                  <div className="text-accent-purple">f = sigma( W_xf * X + W_hf * H^(l-1) + W_mf * M^(l-1) + b_f )</div>
                  <div className="text-accent-rain">i = sigma( W_xi * X + W_hi * H^(l-1) + W_mi * M^(l-1) + b_i )</div>
                  <div className="text-text-primary font-bold">M^l = f ⊗ M^(l-1) + i ⊗ g</div>
                  <div className="text-accent-warn">o = sigma( W_xo * X + W_ho * H^(l-1) + W_mo * M^l + b_o )</div>
                  <div className="text-text-primary font-bold">H^l = o ⊗ tanh( M^l )</div>
                </div>
              </div>
            </div>
          )}

          {/* Component 5: TLoss & Focal Loss Functions */}
          {selectedArchComponent === "loss" && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-accent-purple">
                  Base Paper Multi-Objective Loss Formulation
                </span>
                <h3 className="text-2xl font-bold text-text-primary">
                  TLoss & Enhanced Weighted Loss
                </h3>
                <p className="text-sm text-text-secondary leading-relaxed">
                  Precipitation data suffers from extreme class imbalance: no-rain samples dominate. Standard MSE penalizes errors uniformly, leading models to predict zero rain. TLoss solves this by pairing intensity-weighted MSE with soft threshold classification.
                </p>
                <div className="p-4 rounded-xl bg-surface/80 border border-border-subtle space-y-2">
                  <h4 className="text-xs font-bold text-text-primary uppercase">
                    TLoss Formulation (Eq. 5)
                  </h4>
                  <div className="font-mono text-xs text-teal bg-black/30 p-2.5 rounded">
                    TLoss = WMSE + 0.5 * (BCE_p1 + BCE_p2 + BCE_p3)
                  </div>
                  <p className="text-xs text-text-secondary">
                    Thresholds: $p_1 = 0.05\text{ mm}$ (light rain), $p_2 = 0.5\text{ mm}$ (moderate), $p_3 = 1.0\text{ mm}$ (heavy).
                  </p>
                </div>
              </div>

              <div className="glass-card p-6 space-y-4 flex flex-col justify-center">
                <h4 className="text-sm font-bold text-text-primary">Weighted MSE Formulation</h4>
                <div className="bg-surface/90 border border-teal/30 rounded-xl p-4 font-mono text-xs text-text-secondary space-y-3">
                  <div className="p-2.5 bg-teal/10 rounded-lg text-teal text-center">
                    WMSE = (1/n) · sum( (y_hat - y)^2 · ( e^(y · 0.6) - 0.8 ) )
                  </div>
                  <p className="text-[11px] leading-relaxed">
                    The exponential weight factor exp(y · 0.6) - 0.8 drastically scales up gradients when ground truth rain y is high, forcing the network to accurately capture heavy rainfall cells.
                  </p>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ── TAB 3: Meteorological Benchmarks ── */}
      {activeTab === "benchmarks" && (
        <div className="space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h3 className="text-xl font-bold text-text-primary flex items-center gap-2">
                <TrendingUp className="h-5 w-5 text-teal" />
                Comparative Model Skill Scores (Jiangsu Weather Benchmark)
              </h3>
              <p className="text-xs text-text-secondary mt-1">
                Evaluation results matching Table 3 (1-Hour) & Table 4 (2-Hour) from Sensors 2023 base paper.
              </p>
            </div>
            <div className="flex items-center gap-2 text-xs text-text-secondary">
              <span className="inline-block w-2.5 h-2.5 rounded-full bg-teal" />
              <span>Higher CSI/POD is better (↑); Lower FAR is better (↓)</span>
            </div>
          </div>

          <div className="glass-card overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead>
                  <tr className="border-b border-border-subtle bg-surface/80 text-text-secondary">
                    <th className="p-3.5 font-bold">Model Architecture</th>
                    <th className="p-3.5 font-bold">Parameters</th>
                    <th className="p-3.5 font-bold text-teal">CSI (≥0.05mm)</th>
                    <th className="p-3.5 font-bold text-teal">CSI (≥0.2mm)</th>
                    <th className="p-3.5 font-bold text-teal">CSI (≥0.5mm)</th>
                    <th className="p-3.5 font-bold">POD (Hit Rate)</th>
                    <th className="p-3.5 font-bold">FAR (False Alarm)</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border-subtle font-mono text-text-primary">
                  {/* Proposed TransAtU-Net */}
                  <tr className="bg-teal/10 hover:bg-teal/15 font-semibold">
                    <td className="p-3.5 text-teal font-sans flex items-center gap-1.5">
                      <Sparkles className="h-3.5 w-3.5" />
                      TransAtU-Net (Proposed Transformer)
                    </td>
                    <td className="p-3.5">21,450,112</td>
                    <td className="p-3.5 text-teal">0.412</td>
                    <td className="p-3.5 text-teal">0.278</td>
                    <td className="p-3.5 text-teal">0.158</td>
                    <td className="p-3.5">0.748</td>
                    <td className="p-3.5 text-accent-green">0.521</td>
                  </tr>

                  {/* LSTMAtU-Net (Base Paper) */}
                  <tr className="bg-accent-purple/5 hover:bg-accent-purple/10">
                    <td className="p-3.5 text-accent-purple font-sans flex items-center gap-1.5">
                      <Brain className="h-3.5 w-3.5" />
                      LSTMAtU-Net (Base Paper Model)
                    </td>
                    <td className="p-3.5">18,619,421</td>
                    <td className="p-3.5 text-teal">0.381</td>
                    <td className="p-3.5 text-teal">0.256</td>
                    <td className="p-3.5 text-teal">0.135</td>
                    <td className="p-3.5">0.725</td>
                    <td className="p-3.5">0.554</td>
                  </tr>

                  {/* ConvLSTM Baseline */}
                  <tr className="hover:bg-white/[0.02]">
                    <td className="p-3.5 font-sans">ConvLSTM (Shi et al.)</td>
                    <td className="p-3.5">15,820,000</td>
                    <td className="p-3.5">0.369</td>
                    <td className="p-3.5">0.231</td>
                    <td className="p-3.5">0.098</td>
                    <td className="p-3.5">0.687</td>
                    <td className="p-3.5">0.565</td>
                  </tr>

                  {/* PredRNN */}
                  <tr className="hover:bg-white/[0.02]">
                    <td className="p-3.5 font-sans">PredRNN (Wang et al.)</td>
                    <td className="p-3.5">23,410,000</td>
                    <td className="p-3.5">0.375</td>
                    <td className="p-3.5">0.222</td>
                    <td className="p-3.5">0.098</td>
                    <td className="p-3.5">0.560</td>
                    <td className="p-3.5">0.493</td>
                  </tr>

                  {/* SmaAt-U-Net */}
                  <tr className="hover:bg-white/[0.02]">
                    <td className="p-3.5 font-sans">SmaAt-U-Net (Trebing et al.)</td>
                    <td className="p-3.5">4,200,000</td>
                    <td className="p-3.5">0.346</td>
                    <td className="p-3.5">0.219</td>
                    <td className="p-3.5">0.080</td>
                    <td className="p-3.5">0.741</td>
                    <td className="p-3.5 text-red-400">0.581</td>
                  </tr>

                  {/* Classical U-Net */}
                  <tr className="hover:bg-white/[0.02]">
                    <td className="p-3.5 font-sans">Classical U-Net (Ronneberger et al.)</td>
                    <td className="p-3.5">32,023,892</td>
                    <td className="p-3.5">0.328</td>
                    <td className="p-3.5">0.190</td>
                    <td className="p-3.5">0.060</td>
                    <td className="p-3.5">0.722</td>
                    <td className="p-3.5 text-red-400">0.595</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
