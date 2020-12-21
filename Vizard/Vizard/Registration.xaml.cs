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
using Newtonsoft.Json;
using Vizard.Models;

namespace Vizard
{
    /// <summary>
    /// Interaction logic for Registration.xaml
    /// </summary>
    public partial class Registration : Window
    {
        public Registration()
        {
            InitializeComponent();
        }

        private async void button_Click(object sender, RoutedEventArgs e)
        {
            string name = textBox.Text;
            string email = textBox1.Text;
            string avatar = textBox2.Text;
            string password = passwordBox.Password;

            var user = new User(name, email, password, avatar);

            var json = JsonConvert.SerializeObject(user);

            var res = await Service.Requests.Post(Consts.ConstantSettings.PostUser, json);

            if (res.Contains("OK"))
            {
                MessageBox.Show("OK");
            }

            else
            {
                MessageBox.Show("Input another email");
            }

        }
    }
}
