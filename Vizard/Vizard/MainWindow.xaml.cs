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

namespace Vizard
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        

        public MainWindow()
        {
            var loginWindow = new Login();
            loginWindow.ShowDialog();

            InitializeComponent();
            this.updateEntities();

            if(ApplicationConsts.User != null)
            {
                this.updateAccount();
            }
        }

        async void updateEntities()
        {
            string gamesJson = await Requests.Get(ConstantSettings.GetGames);
            string studiosJson = await Requests.Get(ConstantSettings.GetStudios);
            string genresJson = await Requests.Get(ConstantSettings.GetGenres);
            string usersJson = await Requests.Get(ConstantSettings.GetUsers);

            List<Game> games = JsonConvert.DeserializeObject<List<Game>>(gamesJson);
            List<Studio> studios = JsonConvert.DeserializeObject<List<Studio>>(studiosJson);
            List<Genre> genres = JsonConvert.DeserializeObject<List<Genre>>(genresJson);
            List<User> users = JsonConvert.DeserializeObject<List<User>>(usersJson);


            List<GameView> gamesView = await EntityConverter.ToGamesView(games);
            List<StudioView> studiosView = EntityConverter.ToStudiosView(studios);
            List<GenreView> genresView = EntityConverter.TeGenresView(genres);
            List<UserView> usersView = EntityConverter.ToUsersView(users);

            
            dataGridGames.ItemsSource = gamesView;
            dataGridStudios.ItemsSource = studiosView;
            dataGridGenres.ItemsSource = genresView;
            dataGridUsers.ItemsSource = usersView;
        }

        async void updateAccount()
        {
            if(ApplicationConsts.User.Avatar != "")
            {
                BitmapImage bitmap = DataHandler.GetPictureBitmap(ApplicationConsts.User.Avatar);
                userAvatar.Source = bitmap;
            }            

            labelName.Content = ApplicationConsts.User.Name;
            labelEmail.Content = ApplicationConsts.User.Email;

            List<Game> games = await getUserGamesAsync(ApplicationConsts.User.Id);
            List<GameView> gamesView = await EntityConverter.ToGamesView(games);

            dataGridUserGames.ItemsSource = gamesView;
        }

        async Task<List<Game>> getUserGamesAsync(int? userId)
        {
            string gamesJson = await Requests.Get(ConstantSettings.GetUserGames + $"{userId}/");
            List<Game> games = JsonConvert.DeserializeObject<List<Game>>(gamesJson);

            return games;
        }

        void updateEverything()
        {
            updateEntities();
            updateAccount();
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            var editWindow = new EditUser();
            editWindow.ShowDialog();
            updateEverything();
        }

        async void showUser(User user)
        {
            if (user.Avatar != "")
            {
                imageUserAvatar.Source = DataHandler.GetPictureBitmap(user.Avatar);
            }

            if(!string.IsNullOrEmpty(user.Telegram))
            {
                imageTelegram.Source = DataHandler.GetPictureBitmap(ConstantSettings.TelegramPicture);
                labelUserTeleram.Content = user.Telegram;
            }
            else
            {
                imageTelegram.Source = null;
                labelUserTeleram.Content = null;
            }

            if (!string.IsNullOrEmpty(user.Steam))
            {
                imageSteam.Source = DataHandler.GetPictureBitmap(ConstantSettings.SteamPicture);
            }
            else
            {
                imageSteam.Source = null;
            }

            labelUserName.Content = user.Name;
            labelUserEmail.Content = user.Email;

            var games = await getUserGamesAsync(user.Id);

            dataGridSelectedUserGames.ItemsSource = await EntityConverter.ToGamesView(games);


        }

        private async void dataGridUsers_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            UserView userView = (UserView)dataGridUsers.SelectedValue;
            
            if(userView == null)
            {
                return;
            }

            string userJson = await Requests.Get(ConstantSettings.GetUserId + $"{userView.Id}/");

            User user = JsonConvert.DeserializeObject<User>(userJson);

            this.showUser(user);
        }

        private async void imageSteam_MouseDown(object sender, System.Windows.Input.MouseButtonEventArgs e)
        {
            UserView userView = (UserView)dataGridUsers.SelectedValue;

            string userJson = await Requests.Get(ConstantSettings.GetUserId + $"{userView.Id}/");

            User user = JsonConvert.DeserializeObject<User>(userJson);

            System.Diagnostics.Process.Start(user.Steam);
        }

        private void dataGridGenres_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            GenreView genre = (GenreView)dataGridGenres.SelectedItem;
            this.updateGenre(genre);
        }

        async void updateGenre(GenreView genreView)
        {
            var genreJson = await Requests.Get(ConstantSettings.GetGenreId + $"{genreView.Id}/");
            Genre genre = JsonConvert.DeserializeObject<Genre>(genreJson);

            labelGenreName.Content = genre.Name;
            textBlockGenreDescription.Text = genre.Description;
        }

        private void dataGridStudios_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            StudioView studioView = (StudioView)dataGridStudios.SelectedItem;
            this.updateStudio(studioView);
        }

        async void updateStudio(StudioView studioView)
        {
            var studioJson = await Requests.Get(ConstantSettings.GetStudioId + $"{studioView.Id}/");
            Studio studio = JsonConvert.DeserializeObject<Studio>(studioJson);

            labelStudioName.Content = studio.Name;
            textBlockStudioDescription.Text = studio.Description;

            imageStudioAvatar.Source = DataHandler.GetPictureBitmap(studio.Avatar);

            var gamesJson = await Requests.Get(ConstantSettings.GetStudioGames + $"{studioView.Id}/");
            List<Game> games = JsonConvert.DeserializeObject<List<Game>>(gamesJson);

            List<GameView> gamesView = await EntityConverter.ToGamesView(games);

            dataGridStudioGames.ItemsSource = gamesView;
        }
    }
}
