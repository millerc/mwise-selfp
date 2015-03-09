from django.db.models import Model, CharField, ForeignKey, DateTimeField

from core.models import RoleType, StatusType
from profiles.models import Profile

class Party(Model):
    profile = ForeignKey(Profile)
    
    class Meta:
        verbose_name_plural = "parties"

class Organization(Party):
    name = CharField(max_length=255)
    # other org attributes
    
class Person(Party):
    name_current = CharField(max_length=255)
    # other person attributes

    class Meta:
        verbose_name_plural = "people"
    
class PartyType(Model):
    description = CharField(max_length=255)
    
class PartyClassification(Model):
    party = ForeignKey(Party)
    party_type = ForeignKey(PartyType)
    
class PartyRoleType(RoleType):
    pass

class PartyRole(Model):
    party = ForeignKey(Party)
    party_role_type = ForeignKey(PartyRoleType) 
  
class PartyRelationshipType(Model):
    name = CharField(max_length=255)
    description = CharField(null=True,blank=True,max_length=255)
    party_role_type_from = ForeignKey(PartyRoleType, related_name='prt_from_set')
    party_role_type_to = ForeignKey(PartyRoleType, related_name='prt_to_set')

class PartyRelationship(Model):
    party_role_from = ForeignKey(PartyRole, related_name='pr_from_set')
    party_role_to = ForeignKey(PartyRole, related_name='pr_to_set')
    date_from = DateTimeField()
    date_thru = DateTimeField(null=True,blank=True)
    party_relationship_type = ForeignKey(PartyRelationshipType)

class PartyRelationshipStatusType(StatusType):
    pass
    

