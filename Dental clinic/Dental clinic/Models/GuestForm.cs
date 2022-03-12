using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Dental_clinic.Models
{
    public class GuestResponse
    {
        
            [Required(ErrorMessage = "Введіть своє прізвище та ім'я")]
            public string Name { get; set; }

            [Required(ErrorMessage = "Введіть свій email")]
            [RegularExpression(".+\\@.+\\..+", ErrorMessage = "Ви ввели некоректний email")]
            public string Email { get; set; }

            [Required(ErrorMessage = "Введіть свій номер телефона ")]
            public string Phone { get; set; }

           




    }
}