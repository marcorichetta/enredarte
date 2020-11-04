# Jazzmin Admin settings
# ------------------------------------------------------------------------------

JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "Panel de Administración",
    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Administración",
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "/images/logo.svg",
    # Welcome text on the login screen
    "welcome_sign": "Bienvenido al panel de administración",
    # Copyright on the footer
    "copyright": "Enredarte SRL",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Volver al sitio", "url": "core:home", "new_window": True},
        # external url that opens in a new window (Permissions can be added)
        {"name": "Soporte", "url": "https://marcorichetta.now.sh", "new_window": True},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "compras"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        {"name": "Soporte", "url": "https://marcorichetta.now.sh", "new_window": True},
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [
        "Compras.InsumosCompra",
        "Pedidos.ProductosPedido",
        "Productos.InsumosProducto",
    ],
    # List of apps to base side menu (app or model) ordering off of
    "order_with_respect_to": [
        "variables",
        "pedidos",
        "compras",
        "productos",
        "clientes",
        "proveedores",
        "core",
    ],
    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "polls": [
    #         {
    #             "name": "Make Messages",
    #             "url": "make_messages",
    #             "icon": "fas fa-comments",
    #             "permissions": ["polls.view_poll"],
    #         }
    #     ]
    # },
    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        "clientes.Cliente": "fas fa-users",
        "compras.Compra": "fas fa-dollar-sign",
        "core.Provincia": "fas fa-map-marker-alt",
        "core.Localidad": "fas fa-map-marker-alt",
        "pedidos.Pedido": "fas fa-shopping-cart",
        "productos.Insumo": "fas fa-toolbox",
        "productos.Producto": "fas fa-shopping-bag",
        "productos.Unidad": "fas fa-ruler-horizontal",
        "productos.StockInsumo": "fas fa-boxes",
        "proveedores.Proveedor": "fas fa-phone-alt",
        "variables.Variable": "fas fa-coins",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-dot-circle",
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "vertical_tabs", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-warning navbar-light",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
}
