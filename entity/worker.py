from entity.target import Target

class Worker(Target):

    id = ''
    account = ''
    employer = ''
    created_at = ''
    updated_at = ''
    first_name = ''
    last_name = ''
    full_name = ''
    email = ''
    picture_url = ''
    phone_number = ''
    address =  {
            'line1' : '',
            'line2' : '',
            'city' : '',
            'postal_code' : '',
            'country' :''
        }
    employment_status = ''
    employment_type = ''
    job_title = ''
    ssn = ''
    platform_user_id = ''
    hire_dates = ''
    #terminations = [{NOT_AVAILABLE}]
    marital_status = ''

    def serialize(self):
        """
        serialize object and store in pickle file
        """
        super().serialize(self.full_name)