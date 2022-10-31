using MongoDB.Driver;

namespace dotnetnew.Data.Interfaces
{
    public interface IGateway
    {
        IMongoDatabase GetMongoDB();
    }
}
