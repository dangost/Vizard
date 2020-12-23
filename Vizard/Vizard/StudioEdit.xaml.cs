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
using Vizard.View;
using Vizard.Service;
using Vizard.Consts;
using Vizard.Converters;
using Newtonsoft.Json;

namespace Vizard
{
    /// <summary>
    /// Interaction logic for StudioEdit.xaml
    /// </summary>
    public partial class StudioEdit : Window
    {
        Studio studio;
        int? _studioId;

        public StudioEdit(int studioId = -1)
        {
            InitializeComponent();

            _studioId = studioId;
            if (studioId == -1)
            {
                //creating
                button.Content = "Add";
            }
            else
            {
                setWindow(studioId);
            }
        }

        private async void button_Click(object sender, RoutedEventArgs e)
        {
            string avatar = avatarTextbox.Text;
            string name = nameTextbox.Text;
            string description = descriptionTextbox.Text;
            Studio studio = new Studio(name,avatar, description);
            studio.Id = 0;
            string newStudioJson = JsonConvert.SerializeObject(studio);

            string response;
            if (_studioId == -1)
            {
                response = await Requests.Post(ConstantSettings.GetStudioId, newStudioJson);
            }
            else
            {
                response = await Requests.Put(ConstantSettings.GetStudioId + $"{_studioId}/", newStudioJson);
            }

            if (response.Contains("OK"))
            {
                MessageBox.Show("Succsess");
                Close();
            }
            else
            {
                MessageBox.Show("Problems");
                return;
            }
        }

        async void setWindow(int? studioId)
        {
            string studioJson = await Requests.Get(ConstantSettings.GetStudioId + $"{studioId}/");

            studio = JsonConvert.DeserializeObject<Studio>(studioJson);

            avatarTextbox.Text = studio.Avatar;
            nameTextbox.Text = studio.Name;
            descriptionTextbox.Text = studio.Description;
        }
    }
}
