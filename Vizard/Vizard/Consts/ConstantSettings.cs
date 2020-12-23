using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Consts
{
    public class ConstantSettings
    {
        public const string IP = @"http://127.0.0.1:5000";

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

        public static string TorrentPicture = "https://avatars.mds.yandex.net/get-zen_doc/1904927/pub_5e74af25bc286c6a447ea78e_5e74b6f82cb8ec61326149cb/scale_1200";

        public static string Play = "https://sun9-8.userapi.com/c628827/u192419046/video/y_342f1673.jpg";
    }
}
