from Base.base_page import BasePage
from Pages.POM.auth import Auth
from Pages.POM.signIn import SignInUpClass
from Pages.POM.navigationMenu import NavigationMenu
from Pages.POM.profile_menu_page import ProfileMenu
from Pages.POM.searchPanelPage import SearchEventMenu
from Pages.POM.categories import Categories
from Pages.ProfileMenu.add_event import CreateEvents
from Pages.POM.event_menu_page import EventsMenu
# EventsMenuCarts
from Pages.POM.contact_us_page import ContactUs


class InstantiatePages():
    '''Instantiating a class by making a composition'''

    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.base = BasePage(self.driver_init)
        self.auth = Auth(self.base)
        self.signin = SignInUpClass(self.base)
        self.navigation = NavigationMenu(self.base)
        self.categories = Categories( self.base )
        # page opended from navigation menu
        self.prof_menu = ProfileMenu(self.base)
        self.creat_event = CreateEvents(self.base)
        # search event panel
        self.search = SearchEventMenu(self.base)
        self.contact = ContactUs(self.base)
        self.event_menu = EventsMenu(self.base)
        # self.event_carts = EventsMenuCarts(self.base)