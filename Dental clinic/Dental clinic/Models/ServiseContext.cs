using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using WebUI.Models;

namespace Dental_clinic.Models
{
    public class ServiceContext : DbContext
    {
        public ServiceContext() : base("ServicessDB")
        {

        }

        public DbSet<Service> Servises { get; set; }
        public DbSet<User> Users { get; set; }
        public DbSet<Role> Roles { get; set; }

        //public class ServiceDbInitializer : DropCreateDatabaseAlways<ServiceContext>
        //{
        //    protected override void Seed(ServiceContext db)
        //    {
        //        db.Servises.Add(new Service { Name = "Консультація", Price = 220 });
        //        db.Servises.Add(new Service { Name = "Пломбування", Price = 180 });
        //        db.Servises.Add(new Service { Name = "Видалення зуба", Price = 150 });

        //        base.Seed(db);

        //        Role admin = new Role { Name = "admin" };
        //        Role user = new Role { Name = "user" };
        //        db.Roles.Add(admin);
        //        db.Roles.Add(user);
        //        db.Users.Add(new User
        //        {
        //            Email = "DentalAdmin",
        //            Password = "123456",
        //            Role = admin
        //        });
        //        base.Seed(db);
        //    }
        //}

        

        }

    }


