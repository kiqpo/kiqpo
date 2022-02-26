def topNav(Title="", fillColor="var(--primary);"):
    return f"""<header style='background-color:{fillColor};' class="mdc-top-app-bar">
        <div class="mdc-top-app-bar__row">
            <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
                <button class="material-icons mdc-top-app-bar__navigation-icon mdc-icon-button"
                    aria-label="Open navigation menu">menu</button>
                <span class="mdc-top-app-bar__title">{Title}</span>
            </section>

        </div>
    </header>"""


            # """<section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" role="toolbar">
            #     <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button"
            #         aria-label="Favorite">favorite</button>
            #     <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button"
            #         aria-label="Search">search</button>
            #     <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button"
            #         aria-label="Options">more_vert</button>
            # </section>"""