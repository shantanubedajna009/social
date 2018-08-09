from django.contrib import admin
from groups.models import Group, GroupMember

# Register your models here.

# this is not exactly nessesary just needed for
# because when we are in the admin panel then we can click on the
# group name and on the same page we can see the group members and edit them
# so this is for just convinience we cound have done it with admin.site.register(GroupMember) also
class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
