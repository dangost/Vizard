using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Models
{
    class Game
    {
        public Game(string name, string avatar, string trailer, string description, 
            string platform, string steam, string torrent, float rate, float price, int studioId, int genreId, string systemReq)
        {
            Id = null;
            Name = name;
            Avatar = avatar;
            Trailer = trailer;
            Description = description;
            Platform = platform;
            Steam = steam;
            Torrent = torrent;
            Rate = rate;
            Price = price;
            StudioId = studioId;
            GenreId = genreId;
            SystemRequirements = systemReq;
        }

        public int? Id { get; set; }

        public string Name { get; set; }

        public string Avatar { get; set; }

        public string Trailer { get; set; }

        public string Description { get; set; }

        public string Platform { get; set; }

        public string Steam { get; set; }

        public string Torrent { get; set; }

        public float Rate { get; set; }

        public float Price { get; set; }

        public int StudioId { get; set; }

        public int GenreId { get; set; }

        public string SystemRequirements { get; set; }
    }
}
