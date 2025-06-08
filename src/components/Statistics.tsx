import { Card, CardContent } from "@/components/ui/card";

const Statistics = () => {
  const stats = [
    {
      value: "1M+",
      label: "Активных пользователей",
      description: "По всему миру",
    },
    {
      value: "₽15B",
      label: "Обработано платежей",
      description: "За последний год",
    },
    {
      value: "150+",
      label: "Стран",
      description: "Где работает сервис",
    },
    {
      value: "5min",
      label: "Время интеграции",
      description: "Среднее время подключения",
    },
  ];

  return (
    <section className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-4 font-montserrat">
            Цифры, которые говорят сами за себя
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Наша платформа обрабатывает миллионы транзакций каждый день,
            обеспечивая надежность и масштабируемость для любого бизнеса
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, index) => (
            <Card
              key={index}
              className="text-center border-none shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2"
            >
              <CardContent className="p-8">
                <div className="text-4xl lg:text-5xl font-bold text-purple-600 mb-3 font-montserrat">
                  {stat.value}
                </div>
                <div className="text-lg font-semibold text-gray-900 mb-2">
                  {stat.label}
                </div>
                <div className="text-gray-600">{stat.description}</div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Statistics;
