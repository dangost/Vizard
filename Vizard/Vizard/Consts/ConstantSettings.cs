using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Consts
{
    public class ConstantSettings
    {
        public const string IP = @"https://vizard-api.herokuapp.com";

        public static string UserLoginCheck = IP + "/api/Users/Login/";

        public static string GetUsers = IP + "/api/Users/";

        public static string GetUserId = IP + "/api/Users/";

        public static string PostUser = IP + "/api/Users/";

        public static string PutUser = IP + "/api/Users/";

        public static string GetGames = IP + "/api/Games/";

        public static string GetStudios = IP + "/api/Studios/";

        public static string GetStudioId = IP + "/api/Studios/";

        public static string GetStudioGames = IP + "/api/Studios/StudioGames/";

        public static string GetGenres = IP + "/api/Genres/";

        public static string GetGenreId = IP + "/api/Genres/";

        public static string GetUserGames = IP + "/api/UsersToGames/UserGames/";

        public static string SteamPicture = "https://logos-download.com/wp-content/uploads/2016/05/Steam_icon_logo_logotype.png";

        public static string TelegramPicture = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png";
    }
}
