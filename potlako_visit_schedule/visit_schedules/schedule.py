from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import crf
from .requisitions import requisitions

# schedule for new participants
schedule1 = Schedule(
    name='schedule',
    verbose_name='Potlako+',
    onschedule_model='potlako_subject.onschedule',
    offschedule_model='potlako_prn.subjectoffstudy',
    consent_model='potlako_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Initial Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1010',
    title='Followup Visit',
    timepoint=1,
    rbase=relativedelta(days=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('unscheduled'),
    facility_name='5-day clinic')

schedule1.add_visit(visit=visit0)
schedule1.add_visit(visit=visit1)
