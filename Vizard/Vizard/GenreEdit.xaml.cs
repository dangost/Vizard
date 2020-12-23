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
using Vizard.View;
using Vizard.Service;
using Vizard.Consts;
using Vizard.Converters;


namespace Vizard
{
    /// <summary>
    /// Interaction logic for GenreEdit.xaml
    /// </summary>
    public partial class GenreEdit : Window
    {
        Genre genre;
        int? _genreId;
        public  GenreEdit(int? genreId = -1)
        {
            InitializeComponent();

            _genreId = genreId;
            if (genreId == -1)
            {
                //creating
                button.Content = "Add";
            }
            else
            {
                
                setWindow(genreId);
            }            
            
        }

        private async void button_Click(object sender, RoutedEventArgs e)
        {
            string name = genreNameTextbox.Text;
            string description = genreDescriptionTextbox.Text;
            Genre genre = new Genre(name, description);
            genre.Id = 0;
            string newGenreJson = JsonConvert.SerializeObject(genre);

            string response;
            if(_genreId == -1)
            {
                response = await Requests.Post(ConstantSettings.GetGenreId, newGenreJson);
            }
            else
            {
                response = await Requests.Put(ConstantSettings.GetGenreId + $"{_genreId}/", newGenreJson);
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

        async void setWindow(int? genreId)
        {
            string genreJson = await Requests.Get(ConstantSettings.GetGenreId + $"{genreId}/");

            genre = JsonConvert.DeserializeObject<Genre>(genreJson);

            genreNameTextbox.Text = genre.Name;
            genreDescriptionTextbox.Text = genre.Description;
        }
    }
}
