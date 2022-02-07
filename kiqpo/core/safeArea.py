def safeArea(*AppContent):
    safeAreaTags = [*AppContent]
    safeAreaTag = ""

    for ele in safeAreaTags:
        safeAreaTag += ele
    return f"""<main class="mdc-top-app-bar--fixed-adjust">
  {safeAreaTag}
</main>"""
