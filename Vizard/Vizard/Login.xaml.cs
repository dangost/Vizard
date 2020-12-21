using System;
using System.Web.UI.WebControls;
using System.Windows;
using Newtonsoft.Json;

namespace Vizard
{
    public partial class Login : Window
    {
        public Login()
        {
            InitializeComponent();
        }

        private void Window_Closed(object sender, EventArgs e)
        {
        }

        private async void button_Click(object sender, RoutedEventArgs e)
        {
            var json = JsonConvert.SerializeObject(new Models.UserAuth(emailTextBox.Text, passwordBox.Password));
            string url = Consts.ConstantSettings.UserLoginCheck;

            var res = await Service.Requests.Post(url, json);

            Models.LoginResponse login = JsonConvert.DeserializeObject<Models.LoginResponse>(res);

            if (!login.Result)
            {
                MessageBox.Show("Incorrect Login or Password");
                return;
            }

            string userJson = await Service.Requests.Get(Consts.ConstantSettings.GetUserId + login.Id.ToString() + "/"); 
            
            Consts.ApplicationConsts.User = JsonConvert.DeserializeObject<Models.User>(userJson);

            Close();

        }
        

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            Window reg = new Registration();
            reg.ShowDialog();
        }
    }
}
