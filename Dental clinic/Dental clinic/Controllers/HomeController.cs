using Dental_clinic.Models;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using System.Web.Security;
using WebUI.Models;

namespace Dentile.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {


            return View();
        }

        public ActionResult Contact()
        {


            return View();
        }

        public ActionResult Services()
        {


            return View();
        }

        public ActionResult Price()
        {

            using (ServiceContext db = new ServiceContext())
            {
                return View(db.Servises.ToList());
            }
        }

        [HttpGet]
        public ViewResult SendingData()
        {
            int hour = DateTime.Now.Hour;
            if (hour < 12)
            {
                ViewBag.Greeting =
                    "Доброго ранку! Залиште нам свої дані і ми обов'язково з Вами зв'яжемося для запису на прийом.";
            }

            ViewBag.Greeting =
                "Доброго дня! Залиште нам свої дані і ми обов'язково з Вами зв'яжемося для запису на прийом.";
            return View();
        }



        [HttpPost]
        public ViewResult SendingData(GuestResponse guest)
        {
            if (ModelState.IsValid)
                // Нужно отправить данные нового гостя по электронной почте 
                // организатору вечеринки.
                return View("Thanks", guest);
            else
                // Обнаружена ошибка проверки достоверности
                return View();
        }

        [Authorize(Roles = "admin")]
        public ActionResult Admin()
        {
            using (ServiceContext db = new ServiceContext())
            {
                return View(db.Servises.ToList());
            }

        }

        public ActionResult Create()
        {

            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "Id,Name,Price")] Service service)
        {
            using (ServiceContext db = new ServiceContext())
            {


                if (ModelState.IsValid)
                {
                    db.Servises.Add(service);
                    db.SaveChanges();
                }

                return RedirectToAction("Admin");
            }

            return View(service);
        }

        public ActionResult Delete(int? id)
        {
            using (ServiceContext db = new ServiceContext())
            {


                if (id == null)
                {
                    return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
                }

                Service service = db.Servises.Find(id);
                if (service == null)
                {
                    return HttpNotFound();
                }


                return View(service);
            }
        }

        // POST: Books/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            using (ServiceContext db = new ServiceContext())
            {


                Service service = db.Servises.Find(id);
                db.Servises.Remove(service);
                db.SaveChanges();
                return RedirectToAction("Admin");
            }
        }

        public ActionResult Edit(int? id)
        {
            using (ServiceContext db = new ServiceContext())
            {


                if (id == null)
                {
                    return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
                }

                Service service = db.Servises.Find(id);
                if (service == null)
                {
                    return HttpNotFound();
                }

                return View(service);
            }
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,Name,Price")] Service service)
        {
            using (ServiceContext db = new ServiceContext())
            {

                if (ModelState.IsValid)
                {
                    db.Entry(service).State = EntityState.Modified;
                    db.SaveChanges();
                    return RedirectToAction("Admin");
                }

                return View(service);
            }

        }

        public ActionResult Login()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Login(LoginModels model)
        {
            if (ModelState.IsValid)
            {
                // поиск пользователя в бд
                User user = null;
                using (ServiceContext db = new ServiceContext())
                {
                    user = db.Users.FirstOrDefault(u => u.Email == model.Name && u.Password == model.Password);

                }
                if (user != null)
                {
                    FormsAuthentication.SetAuthCookie(model.Name, true);
                    return RedirectToAction("Admin");
                }
                else
                {
                    ModelState.AddModelError("", "Пользователя с таким логином и паролем нет");
                }
            }

            return View(model);
        }

        public ActionResult Register()
        {
            return View();
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Register(RegisterModel model)
        {
            if (ModelState.IsValid)
            {
                User user = null;
                using (ServiceContext db = new ServiceContext())
                {
                    user = db.Users.FirstOrDefault(u => u.Email == model.Name);
                }
                if (user == null)
                {
                    // создаем нового пользователя
                    using (ServiceContext db = new ServiceContext())
                    {
                        db.Users.Add(new User { Email = model.Name, Password = model.Password, Age = model.Age, RoleId = 2});
                        db.SaveChanges();

                        user = db.Users.Where(u => u.Email == model.Name && u.Password == model.Password).FirstOrDefault();
                    }
                    // если пользователь удачно добавлен в бд
                    if (user != null)
                    {
                        FormsAuthentication.SetAuthCookie(model.Name, true);
                        return RedirectToAction("Index", "Home");
                    }
                }
                else
                {
                    ModelState.AddModelError("", "Пользователь с таким логином уже существует");
                }
            }

            return View(model);
        }
        public ActionResult Logoff()
        {
            FormsAuthentication.SignOut();
            return RedirectToAction("Index", "Home");
        }
    }
}
    

