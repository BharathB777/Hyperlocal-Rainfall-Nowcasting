import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "NowCast TN — Hyperlocal Rainfall Nowcasting",
  description:
    "Real-time weather intelligence platform for Tamil Nadu & Puducherry. Fusing IMD, community weather stations, and ECMWF forecasts with AI-powered rainfall nowcasting.",
  keywords: [
    "weather",
    "nowcasting",
    "rainfall",
    "Tamil Nadu",
    "Puducherry",
    "IMD",
    "ECMWF",
    "deep learning",
    "hyperlocal",
  ],
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-surface text-text-primary">
        <Navbar />
        <main className="flex-1 pt-16">{children}</main>

        {/* Footer */}
        <footer className="border-t border-border-subtle bg-surface/80">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="text-sm text-text-secondary">
                © {new Date().getFullYear()}{" "}
                <span className="font-semibold text-text-primary">NowCast TN</span>
                {" "}— Hyperlocal Rainfall Nowcasting
              </div>
              <div className="flex items-center gap-4 text-xs text-text-secondary">
                <span>Data: IMD • Ambient Weather • ECMWF • Open-Meteo</span>
              </div>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
