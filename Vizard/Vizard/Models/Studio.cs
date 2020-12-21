using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Models
{
    class Studio
    {
        public Studio(string name, string avatar, string description)
        {
            Id = null;
            Name = name;
            Avatar = avatar;
            Description = description;
        }

        public int? Id { get; set; }

        public string Name { get; set; }

        public string Avatar { get; set; }

        public string Description { get; set; }
    }
}
