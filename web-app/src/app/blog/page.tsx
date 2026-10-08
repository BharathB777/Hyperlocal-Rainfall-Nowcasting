"use client";

import { useState } from "react";
import ToggleRainfallMap from "@/components/ToggleRainfallMap";
import {
  BookOpen,
  Calendar,
  Clock,
  User,
  Share2,
  Bookmark,
  MessageSquare,
  Sparkles,
  Layers,
  CloudRain,
  ChevronRight,
  TrendingUp,
  AlertCircle,
  MapPin,
} from "lucide-react";

export default function BlogPage() {
  const [activeTab, setActiveTab] = useState<"featured" | "all">("featured");

  return (
    <div className="min-h-screen py-10 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto space-y-12">
      {/* ── Blog Header & Breadcrumbs ── */}
      <div className="space-y-4 border-b border-border-subtle pb-8">
        <div className="flex items-center gap-2 text-xs text-text-secondary">
          <span className="text-teal font-semibold">Weather Intelligence Blog</span>
          <span>/</span>
          <span>Monsoon Bulletins</span>
          <span>/</span>
          <span>24-Hour Multi-Model Guidance</span>
        </div>

        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal/15 border border-teal/30 text-teal text-xs font-bold uppercase tracking-wider">
          <Sparkles className="h-3.5 w-3.5" />
          Featured Meteorological Analysis
        </div>

        <h1 className="text-3xl sm:text-5xl font-black text-text-primary tracking-tight leading-tight">
          Northeast Monsoon Outlook: 24-Hour Multi-Model Rainfall Blend & Convective Nowcast
        </h1>

        <div className="flex flex-wrap items-center gap-4 text-xs text-text-secondary pt-2">
          <div className="flex items-center gap-1.5 font-medium text-text-primary">
            <User className="h-4 w-4 text-teal" />
            <span>COMK / Hyperlocal Intelligence Team</span>
          </div>
          <span>•</span>
          <div className="flex items-center gap-1.5">
            <Calendar className="h-4 w-4 text-text-secondary" />
            <span>October 2026 Monsoon Bulletin</span>
          </div>
          <span>•</span>
          <div className="flex items-center gap-1.5">
            <Clock className="h-4 w-4 text-text-secondary" />
            <span>6 min read</span>
          </div>
          <span className="hidden sm:inline">•</span>
          <div className="flex items-center gap-1.5 text-accent-rain font-semibold">
            <CloudRain className="h-4 w-4" />
            <span>Updated with 00Z / 12Z NWP Model Blends</span>
          </div>
        </div>
      </div>

      {/* ── Article Content ── */}
      <article className="space-y-8 text-text-secondary leading-relaxed">
        {/* Synoptic Overview Card */}
        <div className="p-6 rounded-2xl bg-surface-card border border-teal/30 space-y-3">
          <h2 className="text-lg font-bold text-text-primary flex items-center gap-2">
            <TrendingUp className="h-5 w-5 text-teal" />
            Synoptic Setup: Active Easterly Wave over Southwest Bay of Bengal
          </h2>
          <p className="text-sm">
            Satellite and scatterometer observations indicate an active easterly surge progressing across the Southwest Bay of Bengal towards coastal Tamil Nadu and Puducherry. With favorable low-level speed convergence and deep tropical moisture (precipitable water values exceeding 55mm), widespread rainfall is anticipated over the coastal belt, extending into interior delta districts.
          </p>
        </div>

        {/* ── THE EMBEDDED CHENNAIRAINS REPLICA: TOGGLEABLE RAINFALL MAP & BLEND BUILDER ── */}
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <h2 className="text-xl sm:text-2xl font-black text-text-primary tracking-tight">
                Interactive 24-Hour Rainfall Blend Builder
              </h2>
              <p className="text-xs text-text-secondary mt-0.5">
                Toggle individual models or build custom weighted blends below. Click on any district for localized forecasts.
              </p>
            </div>
            <span className="text-xs text-teal font-medium px-3 py-1 rounded-lg bg-teal/10 border border-teal/20 self-start sm:self-auto">
              Live Interactive Widget
            </span>
          </div>

          {/* EMBEDDED MAP COMPONENT */}
          <ToggleRainfallMap embeddedInBlog={true} />
        </div>

        {/* ── Analytical Discussion: How Data is Blended in Weather Blogs ── */}
        <div className="space-y-6 pt-6">
          <h3 className="text-xl font-bold text-text-primary">
            How Model Blending Works & Why Single Models Fail
          </h3>
          <p className="text-sm leading-relaxed">
            In weather forecasting blogs like <strong className="text-text-primary">Chennai Rains (COMK)</strong>, relying on a single deterministic numerical weather prediction model often leads to forecast errors. Different models carry systematic biases:
          </p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="glass-card p-5 space-y-2">
              <span className="text-xs font-bold text-teal uppercase">ECMWF IFS (9km)</span>
              <p className="text-xs text-text-secondary">
                Excels in resolving sharp coastal moisture convergence, but can occasionally under-predict inland thunderstorm penetration during afternoon convection.
              </p>
            </div>
            <div className="glass-card p-5 space-y-2">
              <span className="text-xs font-bold text-accent-rain uppercase">GFS (NCEP / NOAA 13km)</span>
              <p className="text-xs text-text-secondary">
                Captures broad synoptic rainfall bands well, but exhibits a well-known wet bias over large landmasses, often smoothing out localized extreme rainfall spots.
              </p>
            </div>
            <div className="glass-card p-5 space-y-2">
              <span className="text-xs font-bold text-accent-purple uppercase">TransAtU-Net (Our AI Model)</span>
              <p className="text-xs text-text-secondary">
                Trained on high-resolution radar and station telemetry; accurately pinpoints intense convective cloud bursts and micro-scale rain rate spikes within 0–3 hours.
              </p>
            </div>
          </div>

          <div className="p-5 rounded-2xl bg-white/[0.02] border border-border-subtle space-y-3">
            <h4 className="text-sm font-bold text-text-primary flex items-center gap-2">
              <AlertCircle className="h-4 w-4 text-accent-rain" />
              Regional Rainfall Breakdown for Coastal Tamil Nadu & Puducherry
            </h4>
            <ul className="list-disc list-inside space-y-2 text-xs text-text-secondary pl-2">
              <li>
                <strong className="text-text-primary">Chennai, Tiruvallur & Chengalpattu:</strong> Expect moderate to heavy showers in intermittent spells, with 24-hour accumulations ranging between <strong className="text-teal">45mm to 75mm</strong>.
              </li>
              <li>
                <strong className="text-text-primary">Puducherry, Auroville & Cuddalore:</strong> Direct zone of easterly wave convergence. 24-hour multi-model consensus shows <strong className="text-teal">60mm to 110mm</strong> (Heavy to Very Heavy Rain).
              </li>
              <li>
                <strong className="text-text-primary">Cauvery Delta (Nagapattinam, Thanjavur):</strong> Widespread rains with isolated heavy downpours reaching <strong className="text-teal">70mm to 120mm</strong> along the coastline.
              </li>
              <li>
                <strong className="text-text-primary">Western & Southern Districts (Coimbatore, Madurai):</strong> Mostly light to moderate afternoon or evening thundershowers (15mm to 35mm).
              </li>
            </ul>
          </div>
        </div>

        {/* Technical Data Pipeline Note */}
        <div className="p-6 rounded-2xl bg-midnight/40 border border-border-subtle space-y-3">
          <span className="text-[10px] font-bold uppercase tracking-wider text-teal">
            Technical Architecture Note
          </span>
          <h4 className="text-sm font-bold text-text-primary">
            How Our Platform Blends Multi-Source Data
          </h4>
          <p className="text-xs text-text-secondary leading-relaxed">
            Just like Chennai Rains&apos; custom plot pipelines, our platform automatically ingests GRIB2 model runs from ECMWF Open Data and NOAA NOMADS, aligns them onto a unified regional geospatial grid (0.05° ~ 5 km), and runs our deep learning <strong className="text-teal">TransAtU-Net</strong> nowcaster for immediate sub-hourly refinements. The Rainfall Blend Builder then computes real-time dynamic linear combinations based on user weights.
          </p>
        </div>
      </article>

      {/* ── More Bulletins & Discussion ── */}
      <div className="pt-8 border-t border-border-subtle space-y-6">
        <h3 className="text-xl font-bold text-text-primary">
          Recent Bulletins & Discussions
        </h3>

        <div className="grid md:grid-cols-3 gap-5">
          {[
            {
              title: "Northeast Monsoon 2026 Season Performance & PWS Verification",
              date: "October 03, 2026",
              category: "Monsoon Tracking",
              readTime: "4 min read",
            },
            {
              title: "Deep Dive: Comparing ECMWF vs. GFS 24-Hour Precipitation Bias",
              date: "September 28, 2026",
              category: "Model Comparison",
              readTime: "7 min read",
            },
            {
              title: "How Hyperlocal PWS Networks Uncovered Coastal Convergence in Pondy",
              date: "September 21, 2026",
              category: "Field Observations",
              readTime: "5 min read",
            },
          ].map((post, idx) => (
            <div key={idx} className="glass-card p-5 flex flex-col justify-between group hover:border-teal/50 transition-all cursor-pointer">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-teal/15 text-teal mb-3 inline-block">
                  {post.category}
                </span>
                <h4 className="text-sm font-bold text-text-primary group-hover:text-teal transition-colors">
                  {post.title}
                </h4>
              </div>
              <div className="mt-4 pt-3 border-t border-border-subtle flex items-center justify-between text-[11px] text-text-secondary">
                <span>{post.date}</span>
                <span className="text-teal font-semibold flex items-center gap-1">
                  Read <ChevronRight className="h-3.5 w-3.5" />
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
