"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Cloud,
  LayoutDashboard,
  MapPin,
  BookOpen,
  Activity,
  Brain,
} from "lucide-react";

const NAV_ITEMS = [
  { href: "/", label: "Home", icon: Cloud },
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/forecast", label: "AI Nowcast", icon: Brain },
  { href: "/blog", label: "Blog", icon: BookOpen },
];

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav className="nav-blur fixed top-0 left-0 right-0 z-50 border-b border-border-subtle">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3 group">
            <div className="relative flex h-9 w-9 items-center justify-center rounded-lg bg-gradient-to-br from-teal to-deep-blue shadow-lg group-hover:shadow-[0_0_20px_rgba(28,114,147,0.5)] transition-shadow duration-300">
              <Activity className="h-5 w-5 text-white" strokeWidth={2.5} />
              <div className="absolute -top-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-accent-rain pulse-live" />
            </div>
            <div className="flex flex-col">
              <span className="text-sm font-bold text-text-primary tracking-tight leading-none">
                NowCast
              </span>
              <span className="text-[10px] font-medium text-text-secondary tracking-wider uppercase">
                Tamil Nadu
              </span>
            </div>
          </Link>

          {/* Nav Links */}
          <div className="hidden md:flex items-center gap-1">
            {NAV_ITEMS.map(({ href, label, icon: Icon }) => {
              const isActive = pathname === href;
              return (
                <Link
                  key={href}
                  href={href}
                  className={`
                    relative flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium
                    transition-all duration-200
                    ${isActive
                      ? "text-accent-rain bg-white/5"
                      : "text-text-secondary hover:text-text-primary hover:bg-white/5"
                    }
                  `}
                >
                  <Icon className="h-4 w-4" />
                  {label}
                  {isActive && (
                    <span className="absolute bottom-0 left-1/2 -translate-x-1/2 h-0.5 w-6 rounded-full bg-accent-rain" />
                  )}
                </Link>
              );
            })}
          </div>

          {/* Live Indicator */}
          <div className="flex items-center gap-2">
            <span className="flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-accent-green/30 bg-accent-green/10 text-xs font-medium text-accent-green">
              <span className="h-1.5 w-1.5 rounded-full bg-accent-green pulse-live" />
              LIVE
            </span>
          </div>

          {/* Mobile menu button */}
          <button className="md:hidden flex items-center justify-center h-9 w-9 rounded-lg bg-white/5 text-text-secondary hover:text-text-primary transition-colors">
            <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </nav>
  );
}
