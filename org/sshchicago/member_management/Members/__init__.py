__author__ = 'chris'

class Member(object):

    def __init__(self):
        self._fname = None
        self._lname = None
        self._email = None
        self._active = False

    @property
    def fname(self):
        """First name"""
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value

    @property
    def lname(self):
        """Last name"""
        return self._lname

    @lname.setter
    def lname(self, value):
        self._lname = value

    @property
    def email(self):
        """Email address"""
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = bool(value)

class SilkStartMember(Member):
    """
    A SilkStart member
    """
    def __init__(self):
        self._expiry_date = None
        self._date_joined = None
        self._plan = None
        self._last_login = None
        self._member_type = None
        self._member_category = None

    @property
    def expiry_date(self):
        """Date account is scheduled to expire"""
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value

    @property
    def date_joined(self):
        """Date joined defined in Silkstart"""
        return self._date_joined

    @date_joined.setter
    def date_joined(self, value):
        self._date_joined = value

    @property
    def plan(self):
        """Membership plan defined in SilkStart"""
        return self.plan

    @plan.setter
    def plan(self, value):
        self._plan = value

    @property
    def last_login(self):
        """Last login in SilkStart"""
        return self._last_login

    @last_login.setter
    def last_login(self, value):
        self._last_login = value

    @property
    def member_type(self):
        """Member type (often None)"""
        return self._member_type

    @member_type.setter
    def member_type(self, value):
        self._member_type = value




class IpaMember(Member):
    """
    A member from our FreeIPA server
    """
    def __init__(self):
        self._equipment_cert_url = None
        self._mozilla_open_badge_url = None
        self._rfid_badge_id = None
        self._metal_key_number = None
        self._member_join_date = None
        self._member_termination_date = None
        self._is_federated_with_other_hackerspaces = None
        self._federated_hackerspaces = None


