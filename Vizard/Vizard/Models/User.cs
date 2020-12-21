using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Models
{
    class User
    {
        public User(string name, string email,  string password, string avatar = "", string telegram = "", string steam = "")
        {
            Name = name;
            Email = email;
            AdminLevel = 0;
            Avatar = avatar;
            PassHash = password;
            Telegram = telegram;
            Steam = steam;
        }

        public int? Id { get; set; }

        public string Name { get; set; }

        public string Email { get; set; }

        public int AdminLevel { get; set; }

        public string Avatar { get; set; }

        public string PassHash { get; set; }

        public string Telegram { get; set; }

        public string Steam { get; set; }
    }
}
