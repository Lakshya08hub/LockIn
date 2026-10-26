// Shared nav + footer injected into every page. Keeps branding/links in one place.
const NAV_LINKS = [
  { href: "index.html", label: "Home", page: "home" },
  { href: "dashboard.html", label: "Dashboard", page: "dashboard" },
  { href: "pricing.html", label: "Pricing", page: "pricing" },
  { href: "settings.html", label: "Settings", page: "settings" },
];

function renderNav() {
  const current = document.body.dataset.page;
  const links = NAV_LINKS.map(
    (l) =>
      `<a href="${l.href}" class="nav-link ${l.page === current ? "active" : ""} text-sm">${l.label}</a>`
  ).join("");

  return `
  <header class="sticky top-0 z-50 backdrop-blur bg-white/80 border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-2">
        <span class="w-8 h-8 rounded-lg brand-gradient flex items-center justify-center text-white font-bold text-sm">LI</span>
        <span class="font-bold text-lg tracking-tight">LockIn</span>
      </a>
      <nav class="hidden md:flex items-center gap-8">${links}</nav>
      <div class="flex items-center gap-3">
        <a href="signup.html?mode=login" class="hidden sm:inline-flex nav-link text-sm font-semibold">Log in</a>
        <a href="signup.html" class="btn-primary text-sm !py-2 !px-4">Get started</a>
      </div>
    </div>
  </header>`;
}

function renderFooter() {
  return `
  <footer class="border-t border-slate-200 bg-white">
    <div class="max-w-6xl mx-auto px-6 py-12 grid grid-cols-2 md:grid-cols-4 gap-8">
      <div class="col-span-2 md:col-span-1">
        <div class="flex items-center gap-2 mb-3">
          <span class="w-7 h-7 rounded-lg brand-gradient flex items-center justify-center text-white font-bold text-xs">LI</span>
          <span class="font-bold">LockIn</span>
        </div>
        <p class="text-sm text-slate-500">Catch at-risk students before they fall behind.</p>
      </div>
      <div>
        <h4 class="text-sm font-semibold mb-3">Product</h4>
        <ul class="space-y-2 text-sm text-slate-500">
          <li><a href="dashboard.html" class="hover:text-slate-900">Dashboard</a></li>
          <li><a href="pricing.html" class="hover:text-slate-900">Pricing</a></li>
          <li><a href="report.html" class="hover:text-slate-900">Sample report</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold mb-3">Company</h4>
        <ul class="space-y-2 text-sm text-slate-500">
          <li><a href="#" class="hover:text-slate-900">About</a></li>
          <li><a href="#" class="hover:text-slate-900">Contact</a></li>
          <li><a href="#" class="hover:text-slate-900">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold mb-3">Legal</h4>
        <ul class="space-y-2 text-sm text-slate-500">
          <li><a href="#" class="hover:text-slate-900">Privacy policy</a></li>
          <li><a href="#" class="hover:text-slate-900">Terms of service</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-slate-200 py-6 text-center text-xs text-slate-400">
      &copy; 2026 LockIn. Prototype for academic demonstration &mdash; not a live commercial product.
    </div>
  </footer>`;
}

document.addEventListener("DOMContentLoaded", () => {
  const navSlot = document.getElementById("nav-slot");
  const footerSlot = document.getElementById("footer-slot");
  if (navSlot) navSlot.innerHTML = renderNav();
  if (footerSlot) footerSlot.innerHTML = renderFooter();
});
