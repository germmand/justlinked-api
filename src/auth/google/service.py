import datetime

from src.applicants.models import ApplicantModel

class GoogleApplicantService(object):
    def __init__(self, db_session):
        self.db_session = db_session

    def obtain_applicant(self, google_applicant_data):
        applicant_data = {
            'email': google_applicant_data["emailAddresses"][-1]["value"],
            'fullname': google_applicant_data["names"][-1]["displayName"],
            'birthday': google_applicant_data["birthdays"][-1]["date"],
            'photo': google_applicant_data["photos"][-1]["url"]
        }
        applicant = self.db_session.query(ApplicantModel)\
            .filter_by(email=applicant_data["email"])\
            .first()
        if applicant is not None:
            return applicant
        new_applicant = ApplicantModel()
        new_applicant.email = applicant_data["email"]
        new_applicant.fullname = applicant_data["fullname"]
        new_applicant.photo = applicant_data["photo"]
        new_applicant.birthday = datetime.date(
            applicant_data["birthday"]["year"], 
            applicant_data["birthday"]["month"], 
            applicant_data["birthday"]["day"])
        newly_created_applicant = new_applicant.save()
        return newly_created_applicant