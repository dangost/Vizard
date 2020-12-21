using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;

namespace Vizard.Service
{
    class DataHandler
    {
        public static bool IsAccountExist(string response)
        {
            bool res = false;

            if(response.Contains("True"))
            {
                res = true;
            }

            return res;
        }

        public static BitmapImage GetPictureBitmap(string url)
        {   if(string.IsNullOrEmpty(url))
            {
                return null;
            }

            BitmapImage bitmap = new BitmapImage();
            bitmap.BeginInit();
            bitmap.UriSource = new Uri(url);
            bitmap.EndInit();

            return bitmap;
        }
    }
}
