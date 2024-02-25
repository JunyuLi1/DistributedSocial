# a5.py
# Junyu Li
# junyul24@uci.edu
# junyul031030@gmail.com
# 86676906
"""Module for running GUI"""
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import simpledialog
import ds_messenger
from pathlib import Path
from tkinter import messagebox
import Profile
import OpenWeather
import LastFM
import ds_client


class Body(tk.Frame):
    """Body class"""
    def __init__(self, root, recipient_selected_callback=None):
        """Construct."""
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        self._draw()

    def node_select(self, event):
        """node_select"""
        index = int(self.posts_tree.selection()[0])
        entry = self._contacts[index]
        if self._select_callback is not None:
            self._select_callback(entry)

    def insert_contact(self, contact: str):
        """Inser_contact"""
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        """Inser_contact_tree."""
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)

    def insert_user_message(self, message: str):
        """Insert_user_message."""
        self.entry_editor.insert(1.0, message + '\n',
                                 'entry-right')  # replaced tk.END

    def insert_contact_message(self, message: str):
        """insert_contact_message."""
        self.entry_editor.insert(1.0, message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        """Get text entry."""
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text: str):
        """Set text entry."""
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

    def delete_all_contacts(self):
        """Delete all contacts."""
        self.posts_tree.delete(*self.posts_tree.get_children())
        self._contacts = []

    def _draw(self):
        """Draw"""
        posts_frame = tk.Frame(master=self, width=250, bg='lightblue')
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self,
                               bg="light green", highlightthickness=2)
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0,
                                      height=5, bg='light blue', fg='green')
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0,
                                    height=5, bg='light blue', fg='green')
        self.entry_editor.tag_configure('entry-right', justify='right')
        self.entry_editor.tag_configure('entry-left', justify='left')
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    """Footer"""
    def __init__(self, root, send_callback=None):
        """Construct"""
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        """Send_click"""
        if self._send_callback is not None:
            self._send_callback()

    def _draw(self):
        """Draw"""
        save_button = tk.Button(master=self, text="Send", width=20)
        # the send_click() function.
        save_button.config(command=self.send_click)
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    """NewcontactDialog"""
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        """construct object"""
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        """Body."""
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        # self.password...
        self.password_label = tk.Label(frame, width=30, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30, show='*')
        self.password_entry.insert(tk.END, self.user)
        self.password_entry.pack()

    def apply(self):
        """apply"""
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()


class PublishDialog(tk.simpledialog.Dialog):
    def body(self, master):
        self.title("Publish Message")
        tk.Label(master, text="Enter your message:").pack()
        self.text_input = tk.Text(master, height=10, width=50)
        self.text_input.pack()
        return self.text_input

    def apply(self):
        self.result = self.text_input.get("1.0", tk.END).strip()


class WeatherInputDialog(tk.simpledialog.Dialog):
    def body(self, master):
        self.title("Weather")
        self.zipcode_label = tk.Label(master, width=30, text="Zipcode:")
        self.zipcode_label.pack()
        self.zipcode_input = tk.Entry(master, width=30)
        self.zipcode_input.pack()
        self.country_code_label = tk.Label(master, width=30, text="Country Code:")
        self.country_code_label.pack()
        self.country_code_input = tk.Entry(master, width=30)
        self.country_code_input.pack()
        self.apikey_label = tk.Label(master, width=30, text="API Key:")
        self.apikey_label.pack()
        self.apikey_input = tk.Entry(master, width=30)
        self.apikey_input.pack()

    def apply(self):
        self.zipcode = self.zipcode_input.get()
        self.country_code = self.country_code_input.get()
        self.apikey = self.apikey_input.get()


class LastFMInputDialog(tk.simpledialog.Dialog):
    def body(self, master):
        self.title("LastFM")
        tk.Label(master, text="Enter your API:").pack()
        self.text_input = tk.Text(master, height=10, width=50)
        self.text_input.pack()
        return self.text_input

    def apply(self):
        self.apikey = self.text_input.get("1.0", tk.END).strip()


class MainApp(tk.Frame):
    """MainAPP"""
    def __init__(self, root):
        """init an object."""
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = ''
        self.password = ''
        self.server = ''
        self.recipient = ''
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        # self.direct_messenger = ... continue!
        self.direct_messenger = ds_messenger.DirectMessenger(
            self.server, self.username, self.password)
        self.profile_obj = Profile.Profile()
        self.path = ''
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    def send_message(self):
        """send message"""
        # You must implement this!
        message = self.body.get_text_entry()
        self.publish(message)
        self.direct_messenger.send(message, self.recipient)
        self.check_new()

    def add_contact(self):
        """add contact."""
        # You must implement this!
        # Hint: check how to use tk.simpledialog.askstring to retrieve
        # the name of the new contact, and then use one of the body
        # methods to add the contact to your contact list
        name = tk.simpledialog.askstring(title="Input",
                                         prompt="Enter a username:")
        if name is not None:
            self.body.insert_contact(name)

    def recipient_selected(self, recipient):
        """recipient_selected."""
        self.body.entry_editor.delete(1.0, tk.END)
        self.body.message_editor.delete(1.0, tk.END)
        self.recipient = recipient
        self.profile_obj.load_profile(self.path)
        self.profile_obj.load_profile(self.path)
        content = self.profile_obj.friend_username[recipient]
        for item in content:
            self.body.insert_contact_message(item)

    def configure_server(self):
        """configure_server."""
        self.body.delete_all_contacts()
        self.body.entry_editor.delete(1.0, tk.END)
        self.body.message_editor.delete(1.0, tk.END)
        self.body._contacts = []
        self.profile_obj.friend_username = {}
        self.profile_obj.save_profile(self.path)
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.
        self.direct_messenger = ds_messenger.DirectMessenger(
            self.server, self.username, self.password)
        if self.direct_messenger.get_token() is False:
            messagebox.showerror("Error",
                                 "Incorrect input for connecting server!")
        self.profile_obj.dsuserver = self.server
        self.profile_obj.username = self.username
        self.profile_obj.password = self.password
        self.profile_obj.save_profile(self.path)
        past_data = self.direct_messenger.retrieve_all()
        self.profile_obj.load_profile(self.path)
        self.profile_obj.extract_for_directmessage(past_data)
        self.profile_obj.save_profile(self.path)
        result = self.profile_obj.friend_username.keys()
        for item in result:
            self.body.insert_contact(item)
        self.profile_obj.save_profile(self.path)
        self.check_new()

    def post_online(self):
        dialog = PublishDialog(self)
        message = dialog.result
        if '@weather' in message:
            weather_dialog = WeatherInputDialog(self)
            zipcode = weather_dialog.zipcode
            country_code = weather_dialog.country_code
            apikey = weather_dialog.apikey
            open_weather = OpenWeather.OpenWeather(zipcode, country_code)
            open_weather.set_apikey(apikey)
            open_weather.load_data()
            message = open_weather.transclude(message)
        if '@lastfm' in message:
            last_fm = LastFM.LastFM()
            lastfm_dialog = LastFMInputDialog(self)
            user_input = lastfm_dialog.apikey
            last_fm.set_apikey(user_input)
            last_fm.load_data()
            message = last_fm.transclude(message)
        self.profile_obj.load_profile(self.path)
        newpost = Profile.Post(entry=message)
        self.profile_obj.add_post(newpost)
        self.profile_obj.save_profile(self.path)
        ds_client.send(self.server, 3021, self.username, self.password, message)


    def publish(self, message: str):
        """Publish"""
        # You must implement this!
        self.body.insert_user_message(message)
        self.body.message_editor.delete(1.0, tk.END)

    def check_new(self):
        """Check new"""
        new_data = self.direct_messenger.retrieve_new()
        if len(new_data) > 0:
            self.profile_obj.load_profile(self.path)
            self.profile_obj.extract_for_directmessage(new_data)
            self.profile_obj.save_profile(self.path)
            for item in new_data:
                if item.recipient == self.recipient:
                    self.body.insert_contact_message(item.message)
                if item.recipient not in self.body._contacts:
                    self.body.insert_contact(item.recipient)
        self.after(1000, self.check_new)

    def _draw(self):
        """draw the gui."""
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.new_file)
        menu_file.add_command(label='Open...', command=self.open_file)
        menu_file.add_command(label='Close', command=self.close_file)

        settings_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact',
                                  command=self.add_contact)
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)

        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

        publish_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=publish_menu, label='Publish')
        publish_menu.add_command(label='Post Online',
                                  command=self.post_online)

    def new_file(self):
        """create a new file."""
        self.clear()
        file_path = filedialog.asksaveasfilename(defaultextension='.dsu')
        Path(file_path).touch()
        self.path = file_path
        self.configure_server()
        self.profile_obj.load_profile(self.path)
        self.profile_obj.dsuserver = self.server
        self.profile_obj.username = self.username
        self.profile_obj.password = self.password
        self.profile_obj.save_profile(self.path)
        past_data = self.direct_messenger.retrieve_all()
        self.profile_obj.load_profile(self.path)
        self.profile_obj.extract_for_directmessage(past_data)
        self.profile_obj.save_profile(self.path)
        self.check_new()

    def open_file(self):
        """open a file."""
        self.clear()
        file_path = filedialog.askopenfilename()
        self.path = file_path
        if file_path:
            try:
                self.profile_obj.load_profile(file_path)
            except Profile.DsuFileError:
                messagebox.showerror('Error', 'Invalid dsu file.')
            except Profile.DsuProfileError:
                messagebox.showerror('Error', 'Invalid dsu file.')
            result = self.profile_obj.friend_username.keys()
            for item in result:
                self.body.insert_contact(item)
                self.body._contacts.append(item)
        self.server = self.profile_obj.dsuserver
        self.username = self.profile_obj.username
        self.password = self.profile_obj.password
        self.direct_messenger = ds_messenger.DirectMessenger(
            self.server, self.username, self.password)
        self.check_new()

    def close_file(self):
        """close the window"""
        self.root.destroy()

    def clear(self):
        """clear the gui."""
        self.body.delete_all_contacts()
        self.body.entry_editor.delete(1.0, tk.END)
        self.body.message_editor.delete(1.0, tk.END)
        self.path = ''
        self.server = ''
        self.username = ''
        self.password = ''
        self.recipient = ''
        self.profile_obj = Profile.Profile()
        self.body._contacts = []


def show_popup():
    """show instructions."""
    new_window = tk.Toplevel()
    new_window.title("Instruction")
    new_window.geometry("500x500")
    custom_font = ("Arial", 15)
    popup_label = tk.Label(new_window, text="Instruction:", font=custom_font)
    popup_label.pack(pady=20)
    new_label = tk.Label(
        new_window,
        text="For this Distributed Social Messenger, "
             "you can chat with other people or publish a post online.\n")
    new_label.pack()
    new_label = tk.Label(
        new_window,
        text="To use this media,"
             " you need open a file or create a file first.\n")
    new_label.pack()
    new_label = tk.Label(new_window, text="The close button is "
                                          "used to close the GUI.\n")
    new_label.pack()
    new_label = tk.Label(new_window, text="Configure DS Server is used "
                                          "to set account or change "
                                          "account after step 1.\n")
    new_label.pack()


if __name__ == '__main__':
    main = tk.Tk()
    main.title("Distributed Social Messenger")
    main.geometry("720x480")
    main.option_add('*tearOff', False)
    app = MainApp(main)
    app.after(100, show_popup)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id = main.after(2000, app.check_new)
    print(id)
    main.mainloop()
