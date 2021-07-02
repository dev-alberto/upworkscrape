from entity.target import Target


class Job(Target):

    jobtitle = ''
    jobdescription = ''
    hourlypay = ''
    proposals = ''
    country = ''

    def serialize(self):
        super().serialize(self.jobtitle)