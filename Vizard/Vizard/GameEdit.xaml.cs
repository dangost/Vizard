using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using Newtonsoft.Json;
using Vizard.Models;
using Vizard.View;
using Vizard.Service;
using Vizard.Consts;
using Vizard.Converters;
using System.Windows.Media.Imaging;
using System.Windows.Input;
using System.Diagnostics;

namespace Vizard
{
    public partial class GameEdit : Window
    {
        List<Studio> studios = new List<Studio> { };
        List<Genre> genres = new List<Genre> { };
        public GameEdit()
        {
            InitializeComponent();
            fillForm();
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                createGame();
            }

            catch(Exception)
            {
                createGame();
            }            
        }

        async void createGame()
        {
            string name = nametextBox.Text;
            string avatar = avatartextBox.Text;
            string trailer = trailertextBox.Text;
            string description = descriptiontextBox.Text;
            string platform = platformtextBox.Text;
            string steam = steamtextBox.Text;
            string torrent = torrentextBox.Text;
            float rate = Convert.ToSingle(ratetextBox.Text);
            float price = Convert.ToSingle(pricetextBox.Text);
            string sys = systemtextBox.Text;

            string studioName = comboBox.Text;
            string genreName = comboBox1.Text;

            int? studioId = -1;
            int? genreId = -1;
            foreach (var studio in studios)
            {
                if(studio.Name == studioName)
                {
                    studioId = studio.Id;
                    break;
                }
            }

            foreach (var genre in genres)
            {
                if (genre.Name == genreName)
                {
                    genreId = genre.Id;
                    break;
                }
            }

            Game game = new Game(
                name:name,
                avatar:avatar,
                trailer:trailer,
                description:description,
                platform:platform,
                steam:steam,
                torrent:torrent,
                rate:rate,
                price:price,
                studioId:studioId,
                genreId:genreId,
                systemReq: sys
                );
            game.Id = 0;
            string gameJson = JsonConvert.SerializeObject(game);

            string response = await Requests.Post(ConstantSettings.GetGames, gameJson);
            if(response.Contains("OK"))
            {
                MessageBox.Show("Success");
                Close();
            }

            else
            {
                MessageBox.Show("Error");
                return;
            }

            
            
        }

        async void fillForm()
        {
            string studiosJson = await Requests.Get(ConstantSettings.GetStudios);
            studios = JsonConvert.DeserializeObject<List<Studio>>(studiosJson);

            string genresJson = await Requests.Get(ConstantSettings.GetGenres);
            genres = JsonConvert.DeserializeObject<List<Genre>>(genresJson);

            List<string> vs1 = new List<string> { };
            foreach(var studio in studios)
            {
                vs1.Add(studio.Name);
            }

            List<string> vs2 = new List<string> { };
            foreach (var genre in genres)
            {
                vs2.Add(genre.Name);
            }

            comboBox.ItemsSource = vs1;
            comboBox1.ItemsSource = vs2;

        }
    }
}
