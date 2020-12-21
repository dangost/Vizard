using Newtonsoft.Json;
using System.Collections.Generic;
using Vizard.Models;
using Vizard.View;
using Vizard.Service;
using Vizard.Consts;
using System.Threading.Tasks;


namespace Vizard.Converters
{
    class EntityConverter
    {
        public async static Task<List<GameView>> ToGamesView(List<Game> games)
        {
            List<GameView> gamesView = new List<GameView> { };

            foreach(var game in games)
            {
                string studioJson = await Requests.Get(ConstantSettings.GetStudioId + $"{game.StudioId}/");
                string genreJson = await Requests.Get(ConstantSettings.GetGenreId + $"{game.GenreId}/");
                Studio studio = JsonConvert.DeserializeObject<Studio>(studioJson);
                Genre genre = JsonConvert.DeserializeObject<Genre>(genreJson);

                var gameView = new GameView(
                    id: game.Id,
                    name: game.Name,
                    platform: game.Platform,
                    rate: game.Rate,
                    price: game.Price,
                    studio: studio.Name,
                    genre: genre.Name
                    );
                gamesView.Add(gameView);
            }

            return gamesView;
        }

        public static List<StudioView> ToStudiosView(List<Studio> studios)
        {
            List<StudioView> studioViews = new List<StudioView> { };

            foreach (var studio in studios)
            {
                var studioView = new StudioView(
                    name: studio.Name,
                    id: studio.Id
                    );
                studioViews.Add(studioView);
            }

            return studioViews;
        }

        public static List<GenreView> TeGenresView(List<Genre> genres)
        {
            List<GenreView> genreViews = new List<GenreView> { };

            foreach (var genre in genres)
            {
                var genreView = new GenreView(
                    id: genre.Id,
                    name: genre.Name
                    ); ;
                genreViews.Add(genreView);
            }

            return genreViews;
        }

        public static List<UserView> ToUsersView(List<User> users)
        {
            List<UserView> userViews = new List<UserView> { };

            foreach (var user in users)
            {
                var userView = new UserView(
                    id: user.Id,
                    name: user.Name
                    ); 
                userViews.Add(userView);
            }

            return userViews;
        }
    }
}
