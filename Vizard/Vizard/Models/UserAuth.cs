using Newtonsoft.Json;

namespace Vizard.Models
{
    class UserAuth
    {
        public UserAuth(string email, string pass)
        {
            this.Email = email;
            this.PassHash = pass; // hashing is req
        }

        public string Email { get; set; }

        public string PassHash { get; set; }
    }

    class LoginResponse
    {
        public LoginResponse(int id, bool result)
        {
            Id = id;
            Result = result;
        }

        public int Id { get; set; }

        public bool Result { get; set; }
    }
}
