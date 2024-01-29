import { supabase } from "@/lib/supabase";

export default function Home() {
  const setNewView = async () => {
    const { data, error } = await supabase.from("views").insert({
      random: "random name",
    });

    if (error) console.log(error);
    if (data) console.log(data);
  };
  setNewView();

  return (
    <div>
      <h1>Hey mate</h1>
    </div>
  );
}
