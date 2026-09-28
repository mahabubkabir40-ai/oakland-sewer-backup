/**
 * Static asset site.
 * POST /thank-you drops the form body and returns 303 to /thank-you.
 * GET and HEAD on /x.html, /x/, and /index.html return 301 to the clean URL.
 * Asset paths are passed through so the asset server can answer them.
 */
const ASSET_PREFIXES = ["/css/", "/images/", "/fonts/"];

function isAssetPath(pathname) {
  if (pathname === "/css" || pathname === "/images" || pathname === "/fonts") return true;
  return ASSET_PREFIXES.some((prefix) => pathname.startsWith(prefix));
}

/**
 * Clean path for an HTML duplicate, or null when the request should be served as-is.
 * /page.html, /page/index.html, and /page/ become /page. /index.html becomes /.
 * "/" is never redirected. Files other than HTML are not redirected.
 */
export function canonicalPathname(pathname) {
  if (!pathname || pathname === "/") return null;
  if (isAssetPath(pathname)) return null;

  let path = pathname;
  let changed = false;

  if (path.length > 1 && path.endsWith("/")) {
    const trimmed = path.replace(/\/+$/, "");
    const last = trimmed.split("/").pop() || "";
    // Leave /sitemap.xml/ and similar file URLs alone.
    if (last.includes(".")) return null;
    path = trimmed;
    changed = true;
  }

  if (path.endsWith("/index.html") || path === "/index.html") {
    path = path.slice(0, -"/index.html".length) || "/";
    changed = true;
  } else if (path.endsWith(".html")) {
    path = path.slice(0, -".html".length) || "/";
    changed = true;
  }

  if (!changed) return null;
  if (path === "") path = "/";
  if (!path.startsWith("/")) path = `/${path}`;
  if (path === pathname) return null;
  return path;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, "") || "/";
    if (
      request.method === "POST" &&
      (path === "/thank-you" || path === "/thank-you.html")
    ) {
      // Drop the body. Do not log, store, or reflect form fields.
      return Response.redirect(`${url.origin}/thank-you`, 303);
    }
    if (request.method === "GET" || request.method === "HEAD") {
      const clean = canonicalPathname(url.pathname);
      if (clean) {
        const target = new URL(url.origin);
        target.pathname = clean;
        target.search = url.search;
        return Response.redirect(target.toString(), 301);
      }
    }
    return env.ASSETS.fetch(request);
  },
};
