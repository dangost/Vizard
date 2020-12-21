using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Vizard.Service
{
    class Requests
    {
        public static async Task<string> Get(string url)
        {
            using (var client = new HttpClient())
            {
                var response = await client.GetAsync(url);
                return await response.Content.ReadAsStringAsync();
            }
        }


        public static async Task<string> Post(string url, string json)
        {
            using (var client = new HttpClient())
            {
                var response = await client.PostAsync(url,
                     new StringContent(json, Encoding.UTF8, "application/json"));
                return await response.Content.ReadAsStringAsync();                   
            }
        }
        
        public static async Task<string> Put(string url, string json)
        {
            using (var client = new HttpClient())
            {
                var response = await client.PutAsync(url,
                     new StringContent(json, Encoding.UTF8, "application/json"));
                return await response.Content.ReadAsStringAsync();
            }
        }

        public static async Task<string> Delete(string url)
        {
            using (var client = new HttpClient())
            {
                var response = await client.GetAsync(url);
                return await response.Content.ReadAsStringAsync();
            }
        }
    }
}
