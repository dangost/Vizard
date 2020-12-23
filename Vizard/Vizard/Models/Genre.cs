using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Models
{
    class Genre
    {
        public Genre(string name, string description)
        {
            Name = name;
            Description = description;
        }

        public int? Id { get; set; }

        public string Name { get; set; }

        public string Description { get; set; }
    }
}
