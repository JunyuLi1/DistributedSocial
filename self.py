import ds_messenger
import Profile
obj2 = ds_messenger.DirectMessenger('168.235.86.101', 'nicaiwoshishei', 'buxiangshuohua')
print(obj2.send('newmes7', 'VC1'))
obj = ds_messenger.DirectMessenger('168.235.86.101', 'VC1', 'VC')
prof_obj = Profile.Profile()
prof_obj.load_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\1010.dsu')
past_data = obj.retrieve_all()
new_data = obj.retrieve_new()
print(past_data)
print(new_data)
for item in past_data:
    if item['from'] not in prof_obj.friend_username:
        prof_obj.add_friend_username(item['from'])
        prof_obj.add_history_to_username(item['from'], item['message'])
        prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\1010.dsu')
    else:
        prof_obj.add_history_to_username(item['from'], item['message'])
        prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\1010.dsu')

for item in new_data:
    if item['from'] not in prof_obj.friend_username:
        prof_obj.add_friend_username(item['from'])
        prof_obj.add_history_to_username(item['from'], item['message'])
        prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\1010.dsu')
    else:
        prof_obj.add_history_to_username(item['from'], item['message'])
        prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\1010.dsu')

"""obj = ds_messenger.DirectMessenger()
print(obj.send('woshi10', 'VC1'))
print(obj.retrieve_all())
print(obj.retrieve_new())"""
