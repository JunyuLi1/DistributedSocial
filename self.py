import ds_messenger
import Profile
obj2 = ds_messenger.DirectMessenger('168.235.86.101', 'nicaiwoshishei', 'buxiangshuohua')
print(obj2.send('newmes7', 'VC1'))
obj = ds_messenger.DirectMessenger('168.235.86.101', 'VC1', 'VC')
prof_obj = Profile.Profile()
prof_obj.load_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\bieyongwodehao.dsu')
past_data = obj.retrieve_all()
new_data = obj.retrieve_new()
print(past_data)
print(new_data)
prof_obj.extract_for_directmessage(past_data)
prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\bieyongwodehao.dsu')
prof_obj.extract_for_directmessage(new_data)
prof_obj.save_profile(r'C:\Users\richa\PycharmProjects\Ics32\32assignment\Test\bieyongwodehao.dsu')
"""obj = ds_messenger.DirectMessenger()
print(obj.send('woshi10', 'VC1'))
print(obj.retrieve_all())
print(obj.retrieve_new())"""
