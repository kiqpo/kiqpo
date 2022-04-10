def kiqpoLayout(AppBar,Body):
    """        KiqpoLayout(
            TopAppBar(Title="Kiqpo"),
            Home(
                Text("Hello from Kiqpo")
            ),
        )"""
    return f"""
  {AppBar}  
  <main class="mdl-layout__content">
    <div class="page-content">
        {Body}
    </div>
  </main>
</div>"""