/**
 * Static asset site with one behavior the asset server cannot do:
 * accept the callback form POST and redirect to /thank-you without
 * putting name, phone, or email into the URL.
 */
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
    return env.ASSETS.fetch(request);
  },
};
