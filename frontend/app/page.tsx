"use client";

import { useEffect, useState, useMemo } from "react";
import {
    useReactTable,
    getCoreRowModel,
    getFilteredRowModel,
    flexRender,
    createColumnHelper,
} from "@tanstack/react-table";

type Planificacion = {
    id: number;
    titulo: string;
    año: number;
    tipo_planificacion: string;
    campo_experiencia: string;
    edad_desde: number;
    edad_hasta: number;
    archivo_url: string;
};

const columnHelper = createColumnHelper<Planificacion>();

export default function Home() {
    const [data, setData] = useState<Planificacion[]>([]);
    const [filter, setFilter] = useState("");

    const columns = useMemo(() => [
        columnHelper.accessor("titulo", {
            header: "Título",
        }),
        columnHelper.accessor("año", {
            header: "Año",
        }),
        columnHelper.accessor("tipo_planificacion", {
            header: "Tipo",
        }),
        columnHelper.accessor("campo_experiencia", {
            header: "Campo de Experiencia",
        }),
        columnHelper.accessor("edad_desde", {
            header: "Edad",
            cell: info => `${info.row.original.edad_desde} - ${info.row.original.edad_hasta} años`
        }),
        columnHelper.accessor("archivo_url", {
            header: "Archivo",
            cell: info => <a href={info.getValue()} target="_blank" className="text-blue-600 hover:underline">Ver</a>
        }),
    ], []);

    useEffect(() => {
        fetch("http://localhost:8000/planificaciones")
            .then(res => res.json())
            .then(setData)
            .catch(console.error);
    }, []);

    const table = useReactTable({
        data,
        columns,
        state: {
            globalFilter: filter,
        },
        onGlobalFilterChange: setFilter,
        getCoreRowModel: getCoreRowModel(),
        getFilteredRowModel: getFilteredRowModel(),
    });

    return (
        <main className="min-h-screen bg-gray-50 p-8">
            <div className="max-w-6xl mx-auto bg-white p-6 rounded-xl shadow-sm border">
                <div className="mb-8 flex justify-between items-center">
                    <h1 className="text-3xl font-bold text-gray-800">🎒 Mi Mochila</h1>
                    <div className="flex gap-4">
                        <select
                            value={filter}
                            onChange={e => setFilter(e.target.value)}
                            className="border p-2 rounded-lg bg-white shadow-sm"
                        >
                            <option value="">Todos los tipos</option>
                            <option value="Unidad Didáctica">Unidad Didáctica</option>
                            <option value="Secuencia Didáctica">Secuencia Didáctica</option>
                            <option value="Proyecto">Proyecto</option>
                        </select>
                    </div>
                </div>

                <div className="overflow-x-auto">
                    <table className="w-full text-left border-collapse">
                        <thead>
                            {table.getHeaderGroups().map(headerGroup => (
                                <tr key={headerGroup.id} className="border-b bg-gray-50">
                                    {headerGroup.headers.map(header => (
                                        <th key={header.id} className="p-4 font-semibold text-gray-700">
                                            {flexRender(header.column.columnDef.header, header.getContext())}
                                        </th>
                                    ))}
                                </tr>
                            ))}
                        </thead>
                        <tbody>
                            {table.getRowModel().rows.map(row => (
                                <tr key={row.id} className="border-b hover:bg-gray-50 transition-colors">
                                    {row.getVisibleCells().map(cell => (
                                        <td key={cell.id} className="p-4 text-gray-600">
                                            {flexRender(cell.column.columnDef.cell, cell.getContext())}
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </main>
    );
}
