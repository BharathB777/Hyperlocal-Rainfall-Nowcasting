"use client";

import { useMemo } from "react";
import {
  ResponsiveContainer,
  ComposedChart,
  Line,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import type { WeatherReading } from "@/lib/types";

interface TrendChartProps {
  readings: WeatherReading[];
  height?: number;
}

export default function TrendChart({ readings, height = 320 }: TrendChartProps) {
  const chartData = useMemo(() => {
    return readings.map((r) => ({
      time: new Date(r.timestamp).toLocaleTimeString("en-IN", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      }),
      fullTime: r.timestamp,
      temp_c: r.temp_c,
      humidity_pct: r.humidity_pct,
      rainfall_mm: r.rainfall_mm ?? 0,
      pressure_hpa: r.pressure_hpa,
      wind_speed_kmh: r.wind_speed_kmh,
    }));
  }, [readings]);

  if (chartData.length === 0) {
    return (
      <div className="glass-card flex items-center justify-center p-8" style={{ height }}>
        <p className="text-text-secondary text-sm">No readings available yet. Data will appear after the next ingestion cycle.</p>
      </div>
    );
  }

  return (
    <div className="glass-card p-5">
      <h3 className="text-sm font-semibold text-text-primary mb-4">
        Temperature & Rainfall Trends
      </h3>
      <ResponsiveContainer width="100%" height={height}>
        <ComposedChart data={chartData} margin={{ top: 5, right: 10, bottom: 5, left: -10 }}>
          <defs>
            <linearGradient id="tempGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#FF6B35" stopOpacity={0.8} />
              <stop offset="100%" stopColor="#FF6B35" stopOpacity={0.1} />
            </linearGradient>
            <linearGradient id="rainGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#00D4FF" stopOpacity={0.8} />
              <stop offset="100%" stopColor="#00D4FF" stopOpacity={0.2} />
            </linearGradient>
          </defs>

          <CartesianGrid
            strokeDasharray="3 3"
            stroke="rgba(139, 164, 184, 0.1)"
            vertical={false}
          />

          <XAxis
            dataKey="time"
            tick={{ fontSize: 11, fill: "#8BA4B8" }}
            tickLine={false}
            axisLine={{ stroke: "rgba(139, 164, 184, 0.2)" }}
            interval="preserveStartEnd"
          />

          <YAxis
            yAxisId="temp"
            orientation="left"
            tick={{ fontSize: 11, fill: "#FF6B35" }}
            tickLine={false}
            axisLine={false}
            domain={["auto", "auto"]}
            unit="°"
          />

          <YAxis
            yAxisId="rain"
            orientation="right"
            tick={{ fontSize: 11, fill: "#00D4FF" }}
            tickLine={false}
            axisLine={false}
            domain={[0, "auto"]}
            unit="mm"
          />

          <Tooltip
            contentStyle={{
              background: "rgba(10, 22, 40, 0.95)",
              border: "1px solid rgba(28, 114, 147, 0.3)",
              borderRadius: "12px",
              backdropFilter: "blur(8px)",
              fontSize: "12px",
              color: "#E8F1F8",
              padding: "12px 16px",
            }}
            itemStyle={{ color: "#E8F1F8" }}
            labelStyle={{ color: "#8BA4B8", marginBottom: "4px" }}
            cursor={{ stroke: "rgba(28, 114, 147, 0.3)" }}
          />

          <Legend
            wrapperStyle={{ fontSize: "12px", color: "#8BA4B8" }}
            iconType="circle"
            iconSize={8}
          />

          <Bar
            yAxisId="rain"
            dataKey="rainfall_mm"
            name="Rainfall (mm)"
            fill="url(#rainGradient)"
            radius={[4, 4, 0, 0]}
            barSize={12}
          />

          <Line
            yAxisId="temp"
            type="monotone"
            dataKey="temp_c"
            name="Temperature (°C)"
            stroke="#FF6B35"
            strokeWidth={2.5}
            dot={false}
            activeDot={{
              r: 5,
              fill: "#FF6B35",
              stroke: "#0A1628",
              strokeWidth: 2,
            }}
          />

          <Line
            yAxisId="temp"
            type="monotone"
            dataKey="humidity_pct"
            name="Humidity (%)"
            stroke="#00D4FF"
            strokeWidth={1.5}
            strokeDasharray="5 5"
            dot={false}
            activeDot={{
              r: 4,
              fill: "#00D4FF",
              stroke: "#0A1628",
              strokeWidth: 2,
            }}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  );
}
