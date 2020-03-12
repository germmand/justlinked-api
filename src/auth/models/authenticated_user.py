class AuthenticatedUser(object):
    # This has to match the get_token_claims method from ApplicantModel
    id = None
    email = None
    fullname = None

    def __init__(self, id, email, fullname):
        self.id = id
        self.email = email
        self.fullname = fullname