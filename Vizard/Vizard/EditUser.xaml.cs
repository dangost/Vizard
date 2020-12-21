using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Vizard.Models;
using Vizard.Consts;
using Vizard.Service;
using Newtonsoft.Json;

namespace Vizard
{
    /// <summary>
    /// Interaction logic for EditUser.xaml
    /// </summary>
    public partial class EditUser : Window
    {
        User user;
        public EditUser()
        {
            user = ApplicationConsts.User;
            InitializeComponent();

            textBoxName.Text = user.Name;
            textBoxAvatar.Text = user.Avatar;
            textBoxSteam.Text = user.Steam;
            textBoxTelegram.Text = user.Telegram;
            passwordBox.Password = user.PassHash;
        }

        private async void button_Click(object sender, RoutedEventArgs e)
        {
            string response = await updateUser();

            if(response.Contains("OK"))
            {
                ApplicationConsts.User = user;
                MessageBox.Show("Account has been edited");
                Close();
            }

            else
            {
                MessageBox.Show("Something was wrong");
            }
        }

        async Task<string> updateUser()
        {
            int? id = user.Id;
            string email = user.Email;
            string name = textBoxName.Text;
            string avatar = textBoxAvatar.Text;
            string telegram = textBoxTelegram.Text;
            string steam = textBoxSteam.Text;
            string password = passwordBox.Password;

            user = new User(name, email, password, avatar, telegram, steam); user.Id = id;

            string userJson = JsonConvert.SerializeObject(user);

            string response = await Requests.Put(ConstantSettings.PutUser + $"{user.Id}/", userJson);

            return response;
        }
    }
}
