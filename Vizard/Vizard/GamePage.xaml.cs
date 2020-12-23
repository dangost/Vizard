using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
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
    /// <summary>
    /// Interaction logic for GamePage.xaml
    /// </summary>
    public partial class GamePage : Window
    {
        string steam = "";
        string torrent = "";
        string trailer = "";

        int? _gameId;
        public GamePage(int? gameId)
        {
            _gameId = gameId;
            InitializeComponent();
            initWindow(gameId);
        }

        async void initWindow(int? gameId)
        {
            Game game;
            Studio studio;
            Genre genre;
            try
            {
                string gameJson = await Requests.Get(ConstantSettings.GetGames + $"{gameId}/");
                game = JsonConvert.DeserializeObject<Game>(gameJson);

                string studioJson = await Requests.Get(ConstantSettings.GetStudioId + $"{game.StudioId}/");
                studio = JsonConvert.DeserializeObject<Studio>(studioJson);

                string genreJson = await Requests.Get(ConstantSettings.GetGenreId + $"{game.GenreId}/");
                genre = JsonConvert.DeserializeObject<Genre>(genreJson);

                if (!string.IsNullOrEmpty(game.Avatar))
                {
                    imageAvatar.Source = DataHandler.GetPictureBitmap(game.Avatar);
                }                    

                if (!string.IsNullOrEmpty(game.Steam))
                {
                    imageSteam.Source = DataHandler.GetPictureBitmap(ConstantSettings.SteamPicture);
                    steam = game.Steam;
                }

                if (!string.IsNullOrEmpty(game.Torrent))
                {
                    imageTorrent.Source = DataHandler.GetPictureBitmap(ConstantSettings.TorrentPicture);
                    torrent = game.Torrent;
                }

                if (!string.IsNullOrEmpty(studio.Avatar))
                {
                    imageStudio.Source = DataHandler.GetPictureBitmap(studio.Avatar);
                }

                if (!string.IsNullOrEmpty(game.Trailer))
                {
                    image.Source = DataHandler.GetPictureBitmap(ConstantSettings.Play);
                    trailer = game.Trailer;
                }


                labelName.Content = game.Name;
                descriptionTextblock.Text = game.Description;
                labelPrice.Content = game.Price + "$";
                systemReq.Text = game.SystemRequirements;
                labelStudioName.Content = studio.Name;
                platformTextblock.Text = game.Platform;
                labelGenre.Content = genre.Name;
            }

            catch (Exception)
            {
                if (MessageBox.Show($"Something was wrong. Do you want to try again?", "Question", MessageBoxButton.YesNo, MessageBoxImage.Warning) == MessageBoxResult.No)
                {
                    initWindow(gameId);
                }
                else
                {
                    MessageBox.Show("Denied");
                    Close();
                }
            }  
        }

        private void imageSteam_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if(imageSteam.Source != null)
            {
                Process.Start(steam);
            }
        }

        private void imageTorrent_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if (imageTorrent.Source != null)
            {
                Process.Start(torrent);
            }
        }

        private void image_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if (image.Source != null)
            {
                Process.Start(trailer);
            }
        }
    }
}
