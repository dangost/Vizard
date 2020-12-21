using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.View
{
    class GameView
    {
        public GameView(int? id, string name, string platform, float rate, float price, string studio, string genre)
        {
            Id = id;
            Name = name;
            Platform = platform;
            Rate = rate;
            Price = price;
            Studio = studio;
            Genre = genre;
        }

        public int? Id { get; set; }
        public string Name { get; set; }

        public string Platform { get; set; }

        public float Rate { get; set; }

        public float Price { get; set; }

        public string Studio { get; set; }

        public string Genre { get; set; }
    }
}
